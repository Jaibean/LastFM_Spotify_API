from flask import Flask, render_template, request, session, redirect
import json, base_file

app = Flask(__name__)

app.secret_key = 'th1s 1s a V3RY s3cure app '


obj = base_file.lastFmSpotify()
topsongs = obj.fetch_songs_from_lastfm()


@app.route('/')
def hello_world():
    return redirect('/create')


@app.route('/top', methods=['GET', 'POST'])
def top_songs():
    if request.method =='GET':
        topsongs = obj.fetch_songs_from_lastfm()
        return render_template("index.html", topsongs=topsongs, template='top')

    else:
        if 'id' in session.keys():
            uri = obj.get_uri_from_spotify(topsongs)
            id = session['id']
            ans = obj.add_songs_to_playlist(id, uri)
            return redirect('/view')
        return redirect('/create')


@app.route('/view' )
def view_songs():
    if 'id' in session.keys():
        songs = obj.list_songs_in_playlist(session['id'])
        return render_template("index.html", songs=song, template='view')
    return redirect('/create')


@app.route('/create', methods=['GET', 'POST'])
def create_playlist():
    # print(request.method)
    if request.method == 'GET':
        return render_template("index.html", template='create')
    if request.method == 'POST':
        name = request.form['playlist_name'].strip()
        desc = request.form['playlist_desc'].strip()
        session['id'] = obj.create_spotify_playlist(name, desc)
        return redirect('/top')


"""@app.route('/name/<user>')
def hello_user(user):
    return render_template("index.html", user=user)
"""
if __name__ == '__main__':
    app.run(debug=True)
