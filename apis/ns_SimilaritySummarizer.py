from flask_restplus import Namespace, Resource, fields
from core.utility import Utility
from werkzeug.datastructures import FileStorage
import uuid , os
from textblob import TextBlob


utils = Utility()
api = Namespace('SimilaritySummarizer',
                description='Sentence Similarity based text summarizer')


upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True, help= 'text file')


@api.route('/upload/')
@api.expect(upload_parser)
class SummarizerSimilarity(Resource):
    @api.response(200, 'Success')
    @api.response(404, 'Validation Error')
    def post(self):
        try:
            args = upload_parser.parse_args()
            uploaded_file = args['file']
            filepath = os.path.join('FileStorage',str(uuid.uuid4())+'.txt')
            uploaded_file.save(filepath)
            result = utils.generate_summary(filepath)
            testimonial = TextBlob(result)
            polarity = testimonial.sentiment.polarity

            return {'SentimentPolarity':polarity, 'Summary':result}
        except:
            api.abort(404)
