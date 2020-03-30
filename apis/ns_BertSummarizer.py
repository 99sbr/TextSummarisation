from flask_restplus import Namespace, Resource, fields
from flask_restplus import reqparse , Api
from werkzeug.datastructures import FileStorage
import uuid , os
from summarizer import Summarizer
from textblob import TextBlob



api = Namespace('BertSummarizer',
                description='Creating semantic summary information from huge corpus of text')


upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True, help= 'text file')


@api.route('/upload/')
@api.expect(upload_parser)
class SummarizerBert(Resource):
    @api.response(200, 'Success')
    @api.response(404, 'Validation Error')
    def post(self):
        try:
            model = Summarizer()
            args = upload_parser.parse_args()
            uploaded_file = args['file']
            filepath = os.path.join('FileStorage',str(uuid.uuid4())+'.txt')
            uploaded_file.save(filepath)
            file = open(filepath, "r")
            filedata = file.read()
            result = model(filedata, min_length=10)
            summary = ''.join(result)
            testimonial = TextBlob(summary)
            polarity = testimonial.sentiment.polarity
            return {'SentimentPolarity':polarity, 'Summary':summary}
        except:
            api.abort(404)
