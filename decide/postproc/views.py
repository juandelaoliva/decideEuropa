from rest_framework.views import APIView
from rest_framework.response import Response


class PostProcView(APIView):

    def identity(self, options):
        for opt in options:
            opt['postproc'] = opt['votes']

        options.sort(key=lambda x: -x['postproc'])
        return Response(options)

    def dhondt(self, options, seats):
        #Se añade un campo de escaños (seats) a cada una de las opciones
        for opt in options:
            opt['seats'] = 0

        #Para cada uno de los escaños se calcula a que opción le correspondería el escaño 
        #teniendo en cuenta los ya asignados
        for i in range(seats):
            max(options, 
                key = lambda x : x['votes'] / (x['seats'] + 1.0))['seats'] += 1

        #Se ordenan las opciones por el número de escaños
        options.sort(key=lambda x: -x['seats'])
        return Response(options)

    def sainteLague(self, options, seats):
        #Se añade un campo de escaños (seats) a cada una de las opciones
        for opt in options:
            opt['seats'] = 0

        #Para cada uno de los escaños se calcula a que opción le correspondería el escaño 
        #teniendo en cuenta los ya asignados
        for i in range(seats):
            max(options, 
                key = lambda x : x['votes'] / (2 * x['seats'] + 1.0))['seats'] += 1

        #Se ordenan las opciones por el número de escaños
        options.sort(key=lambda x: -x['seats'])
        return Response(options)


    def multiQuestions(self, questions):

        for question in questions:
            for option in question:
                option['postproc'] = option['votes'];

            question.sort(key=lambda x: -x['postproc'])

        
        return Response(questions)
        
    def equalityVoting(self, options, seats, method):

        groups = []
        divOptions = {}
        res = []
        #Obtener grupos
        for opt in options:
            g = opt.get("group", "no_group")
            
            if not g in groups: 
                groups.append(g)

        #Inicializar listas de opciones
        for group in groups:
            divOptions[group] = []      

        #Categorizar opciones por grupo
        for opt in options:
            divOptions[opt.get("group", "no_group")].append(opt)

        #Unificar votaciones
        for group in dict(divOptions):
            res = [*res, *method(divOptions[group], seats//len(groups)).data]

        res.sort(key=lambda x: -x['seats'])
        return Response(res)

    def post(self, request):
        """
         * type: IDENTITY | EQUALITY | WEIGHT
         * groups: true
         * options: [
            {
             option: str,
             number: int,
             votes: int,
             ...extraparams
            }
           ]
        """

        t = request.data.get('type', 'IDENTITY')
        groups = request.data.get('groups', False)
        opts = request.data.get('options', [])
        if groups:
            if t == 'DHONDT':
                seats = int(float(request.data.get('seats', '8')))
                return self.equalityVoting(opts, seats, lambda x, y : self.dhondt(x, y))

            elif t == 'SAINTELAGUE':
                seats = int(float(request.data.get('seats', '8')))
                return self.equalityVoting(opts, seats, lambda x, y : self.sainteLague(x, y))

        elif t == 'IDENTITY':
            return self.identity(opts)

        elif t == 'MULTI':
            questions = request.data.get('questions', [])
            return self.multiQuestions(questions)

        elif t == 'DHONDT':
            seats = int(float(request.data.get('seats', '8')))
            return self.dhondt(opts,seats)

        elif t == 'SAINTELAGUE':
            seats = int(float(request.data.get('seats', '8')))
            return self.sainteLague(opts, seats)            

        return Response({})