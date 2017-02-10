from django.db import models


class ImageSet(models.Model):
    # Images for application
    name = models.CharField(max_length=200)


class Image(models.Model):
    parent_set = models.ForeignKey(ImageSet,
                                   on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics/',
                              default='pics/None/no-img.jpg')
    name = models.CharField(max_length=200)
    build_progress = models.IntegerField()
    #   iclass = models.CharField()


'''
# Trying to make the img uploader work as intended first before returning to nns
class Nnet(models.Model):
    structure = models.CharField()


class TrainedNnet(models.Model):
    nnet = models.ForeignKey(Nnet,
                             on_delete=models.CASCADE)
    iset = models.ForeignKey(Iset,
                             on_delete=models.CASCADE)

'''
