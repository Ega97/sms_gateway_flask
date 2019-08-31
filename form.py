from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import data_required ,length, Email,EqualTo

class FormSiswa(FlaskForm):
    nama_siswa = StringField('nama_siswa',validators=[data_required(),length(min =2,max= 50)])
                    
    
    # jenis_kelamin = StringField('jenis_kelamin',
    #                     validators=[data_required(),length(min =2,max= 50)])
    
    # alamat= StringField('alamat',
    #                     validators=[data_required(),length(min =2,max= 50)])
    

    # kelas = StringField('kelas',
    #                     validators=[data_required(),length(min =2,max= 50)])
    
    # no_hp_ortu = StringField('no_hp_ortu',
    #                     validators=[data_required(),length(min =2,max= 50)])
    


class RegistrationForm(FlaskForm):
    username = StringField('username',
                        validators=[data_required(),length(min =2,max= 20)])
    email  = StringField('Email',
                        validators=[data_required(),Email()])
    password = PasswordField('Password',validators=[data_required()])
    confirm_password =PasswordField('Confirm Password',
                        validators=[data_required(),EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm): 
    email  = StringField('Email',
                        validators=[data_required(),Email()])
    password = PasswordField('Password',validators=[data_required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')