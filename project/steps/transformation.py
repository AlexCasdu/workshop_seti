from ant_py import Step, Package, Error


class Transformation(Step):
    # Constantes
    MESSAGES = {"0": "Message with error"}
    def __init__(self, **args):
        super().__init__(**args)

    def __call__(self, package: Package)-> Package:
        try:
            messages = []
            package.status = Package.OK
            package.desc_status = ''

            for line in package.message_in.body:
                messages.append(self.transform_data(line))

            package.general_info["messages"] = len(messages)
            package.message_in.body = messages

        except (RuntimeError, TypeError, NameError, KeyError) as err:
            error = Error()
            error.step = self.name
            error.type = Error.TECNICAL
            error.description = err
            error.body.append(line)
            package.errors.append(error)
            package.status = Package.ERROR
            package.desc_status += self.MESSAGES["0"]

        return package

    @staticmethod
    def transform_data(data):
        date = data['birthdate'].strftime('%Y-%m-%dT%X')
        address = data['address'].replace('\n', ' ')
        structure = f'{data["_id"]} | {data["username"]} | {data["name"]} | {address} | {date} | {data["email"]} | {data["accounts"]}'
        return structure
