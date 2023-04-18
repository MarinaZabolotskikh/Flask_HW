from flask import Flask, jsonify, request
from flask.views import MethodView
from db import AdvertModel, Base, Session
from db import PG_DSN

app = Flask('app')


class AdView(MethodView):

    def get(self, ad_id):
        with Session() as session:
            ad = session.query(AdvertModel).get(ad_id)
            if ad is not None:
                return jsonify({
                    'id': ad.id,
                    'heading': ad.heading,
                    'description': ad.descriotion,
                    'creation_date': ad.creation_date.isoformat(),
                    'owner': ad.owner
                })
            else:
                return jsonify({'message': 'No such ad exists'})

    def post(self):
        with Session() as session:
            ad = AdvertModel(**request.json)
            session.add(ad)
            session.commit()
            return jsonify({'id': ad.id})

    def delete(self, ad_id):
        with Session() as session:
            ad = session.query(AdvertModel).get(ad_id)
            if ad is not None:
                session.delete(ad)
                session.commit()
                return jsonify({'message': 'Ad removed'})
            else:
                return jsonify({'message': 'No such ad exists'})


app.add_url_rule('/ads/', view_func=AdView.as_view('create_ad'), methods=['POST'])
app.add_url_rule('/ads/<int:ad_id>', view_func=AdView.as_view('ads'), methods=['GET', 'DELETE'])
