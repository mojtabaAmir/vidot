from flask import Response, jsonify


class VidotResponse:
    @staticmethod
    def payload(body, meta=None, success=True):
        res = {}
        if success:
            res["data"] = body
        else:
            res["errors"] = body

        if meta:
            res["meta"] = meta
        
        return jsonify(res)

    @classmethod
    def ok(cls, data, meta=None):
        return cls.payload(data, meta), 200

    @classmethod
    def bad_request(cls, errors):
        return cls.payload(errors, success=False), 400
