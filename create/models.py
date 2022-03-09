from django.db import models

# Create your models here.

# create a class to store individuals info
class individual(models.Model):
	first_Name = models.CharField(max_length = 100)
	last_Name = models.CharField(max_length = 100)
	# # dob = models.DateField()

	mother = models.ForeignKey('self', 
		models.SET_NULL, 
		blank=True, 
		null=True,
		related_name='children_of_mother'
		)
	father = models.ForeignKey('self',
		models.SET_NULL,
		blank=True,
		null=True,
		related_name='child_of_father'
		)

	def __str__(self):
		return self.first_Name;
