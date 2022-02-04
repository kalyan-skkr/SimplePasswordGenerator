from flask import Flask, request

from constants import Constants
from passwordGeneratorRepository import PwdGenRepo

app = Flask(__name__)


@app.route('/generatePassword', methods=['GET'])
def generate_password():
    pwdLength, reqLetters = PwdGenRepo.set_password_length(request.args)
    words, oneword = PwdGenRepo.set_required_words(reqLetters, PwdGenRepo.words)

    return PwdGenRepo.genPass(words, oneword, Constants.specialChars, pwdLength)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
