import sys
sys.path.append('./src')
import app

#running the server
if __name__ == '__main__':
    app.app.run(debug=True)