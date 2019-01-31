from apps.user import *

urls = [
    (r"/api/v1/user/auth/login", LoginHandler),
    (r"/api/v1/user/auth/register", RegisterHandler),
    (r"/api/v1/user/auth/forgotpassword", ForgotPasswordHandler),
    (r"/api/v1/user/auth/resetpassword", ResetPasswordHandler)
]
