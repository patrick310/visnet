from django.db import models

class Iset(models.Model)
	#Images for application
	name = models.CharField(max_length=200)

class Image(models.Model)
	iset = models.ForeignKey(Iset,
	on_delete = models.CASCADE)
	name = models.CharField(max_length=200)
	iheight
	iwidth
	op = models.IntegerField( )
	iclass = model.CharField()
	
class Nnet(models.Model)
#Structure of network

class TrainedNnet(models.Model)
	nnet = models.ForeignKey(Nnet,
	on_delete=models.CASCADE)
	iset = models.ForeignKey(Iset,
	on_delete = models.CASCADE)


# Create your models here.
