import codage_predictif_image as pred
import codage_paires_octets_image as paires

nomsImage = ['Image01hyp05.jpg', 'Image02hyp05.jpg', 'Image03hyp05.jpg']

for nom in nomsImage:
    print('-----Image  :', nom)
    print('Predictif  :')
    pred.predictif(nom)
    print('Par paires  :')
    paires.paires(nom)

