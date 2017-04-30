from webargs import fields, validate


features = {
    'barometric': fields.Float(required=True),
    'humidity' : fields.Float(required=True),
    'speed': fields.Float(required=True),
    'temp': fields.Float(required=True),
    'direction':fields.Float(required=True),
    'eff': fields.Float(required=True),
    'panel_area': fields.Float(required=True)
}
