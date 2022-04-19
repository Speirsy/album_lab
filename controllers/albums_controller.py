from flask import Flask, render_template, redirect
from flask import Blueprint
import repositories.album_repository as album_repository

albums_blueprint = Blueprint("albums", __name__)

@albums_blueprint.route("/albums")
def albums():
    albums = album_repository.select_all()
    return render_template ("albums/index.html", all_albums = albums)


@albums_blueprint.route("/albums/<id>", methods=['GET'])
def show_album(id):
    album = album_repository.select(id)
    return render_template('albums/show.html', banana=album )

    # DELETE
# DELETE '/albums/<id>'

# @albums_blueprint.route("/albums/<id>/delete", methods=['POST'])
# def delete_task(id):
#     album_repository.delete(id)
#     return redirect('/album')



