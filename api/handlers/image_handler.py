import tornado.web


class ImageHandler(tornado.web.RequestHandler):
    def initialize(self):
        pass
        # self.fs = GridFS(Connection()['database'], 'imgs')

    def get(self, img_id):
        pass
        # image = self.fs.get(ObjectId(img_id))
        # self.set_header('Content-type', image.content_type)
        # self.set_header('Content-length', image.length)
        # self.write(image.read())
        # self.finish()

    def post(self):
        pass
        # image = self.request.files['files'][0]['body']
        # tipo = self.request.headers['Content-Type']
        # img_id = self.fs.put(image, content_type=tipo)
        # self.write(dumps({"img_id": img_id}))
        # self.finish()
