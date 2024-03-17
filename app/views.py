import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from app.models import PropertyInfo
from app.forms import PropertyForm


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/properties/create', methods=['POST', 'GET'])
def create_property():
    # Instantiate your form class    
    form = PropertyForm()
    
    # Validate file upload on submit
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            bedrooms = form.num_bedrooms.data
            bathrooms = form.num_bathrooms.data
            location = form.location.data.replace(',', '')
            price = form.price.data.replace(',', '')
            type = form.type.data
            description = form.description.data
            
            # Get file data
            pic = form.photo.data # we could also use request.files['photo']
            picfilename = secure_filename(pic.filename)
            pic.save(os.path.join(app.config['UPLOAD_FOLDER'], picfilename))
            
            property = PropertyInfo(
                title = title,
                type = type,
                filename = picfilename,
                bedroom_no = bedrooms,
                bathroom_no = bathrooms,
                price = price,
                location = location,
                description = description
            )
            
            db.session.add(property)
            db.session.commit()
            

            flash('Property Saved', 'success')
            return redirect(url_for('view_properties')) 
        flash_errors(form)
    
    # Validate file upload on submit
    if form.validate_on_submit():
        # Get file data and save to your uploads folder

        flash('Property Saved', 'success')
        return redirect(url_for('view_properties')) 

    return render_template('property_form.html', form=form)


@app.route('/properties')
def view_properties():
    """Render the website's page that displays all properties."""
    properties = db.session.execute(db.select(PropertyInfo)).scalars()  
    #for home in properties:
        #print(home)
    return render_template('properties.html', properties=properties) 


@app.route("/properties/pics/<filename>")
def get_image(filename):
    root_dir = os.getcwd()

    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)


@app.route('/properties/<propertyid>')
def view_property(propertyid):
    """Render the website's page that displays a selected property's details."""    
    property = db.get_or_404(PropertyInfo, propertyid)
    print(property)    
    return render_template('property.html', property=property)
###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

@app.context_processor
def utility_functions():
    def print_in_console(message):
        print (str(message))
        
    return dict(mdebug=print_in_console)
