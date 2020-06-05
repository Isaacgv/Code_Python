import jwt


def create_token(data, secret):
    """ Create JSON Web Token"""

    jwt_token = jwt.encode(data, secret, algorithm='HS256')
    return jwt_token

def verify_signature(token):
    """ Verificate token"""

    key = 'acelera'

    try: 
        return jwt.decode(token, key, verify=True, algorithms='HS256')
    except jwt.InvalidTokenError:
        return {"error": 2}
        
