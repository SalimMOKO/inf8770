import codage_predictif_image as pred

nomsImage = ['Image01hyp01.jpg', 'Image01hyp03.jpg', 'Image02hyp01.jpg', 'Image02hyp03.jpg', 'Image03hyp01.jpg', 'Image03hyp03.jpg']

for nom in nomsImage:
    print('-----Predictif  :')
    print('Image  :', nom)
    pred.predictif(nom)

for
