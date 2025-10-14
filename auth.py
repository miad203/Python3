from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash("Account created successfully!", "info")
        return redirect(url_for('home'))
    return render_template('register.html', form=form, title="Sign Up")


@auth.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'miadac681@gmail.com' and form.password.data == '12345687':
            flash("Successfully logged in!", "success")
            return redirect(url_for('home'))
        else:
            flash('Check your information and try again!', 'danger')
    return render_template('login.html', form=form, title="Log In")


@auth.route('/logout')
def logout():
    # session.pop('email', None)
    # session.pop('password', None)
    flash("You've been logged out!", "primary")
    return redirect(url_for('login'))
