import codage_predictif_image as pred
import codage_paires_octets_image as paires

nomsImage = ['Image01hyp05.jpg', 'Image02hyp05.jpg', 'Image03hyp05.jpg',
             'Image01hyp07.jpg', 'Image02hyp07.jpg', 'Image03hyp07.jpg',
             'Image01hyp03.jpg', 'Image02hyp03.jpg', 'Image03hyp03.jpg']

for nom in nomsImage:
    print('-----Image  :', nom)
    print('Predictif  :')
    pred.predictif(nom)
    print('Par paires  :')
    paires.paires(nom)

