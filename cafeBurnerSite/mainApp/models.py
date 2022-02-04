from django.db import models


class Flyer_Image(models.Model):
    
    # Flyer_image = models.ImageField(upload_to='flyer_imgs/',height_field=None, width_field=None, max_length=200, null = False, blank = False)
    Flyer_image = models.ImageField(upload_to='flyer_imgs/', null = False, blank = False)


class Flyer(models.Model):
    
    
    boros = [('brooklyn', 'Brooklyn'), ('queens','Queens'), ('manhattan','Manhattan'),
                ('bronx','Bronx'), ('staten','Staten Island'), ('nassau','Nassau')]
    Boro = models.CharField(max_length=10, choices=boros)
    
    Event_date = models.DateField()
    
    Flyer_image = models.OneToOneField(Flyer_Image, on_delete=models.CASCADE, primary_key=True,)


    event_types = [('comedy', 'Comedy'), ('food','Food/Drink'), ('athletic','Athletic'),
                ('sports','Sports'), ('seasonal','Seasonal'), ('rock','Live Music: Rock'), 
                ('hipHop','Live Music: HipHop'), ('dance','Live Music: Dance'), ('other','Live Music: Other')]
    Event_type = models.CharField(max_length=10, choices=event_types)

    Contact_information = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)

    pub_date = models.DateTimeField(auto_now_add=True)

    def dayOfWeek(this):
        return this.Event_date.strftime('%A').lower()


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class Reminder(models.Model):

    User_email = models.CharField(max_length=200)
    Flyer = models.ForeignKey(Flyer, on_delete=models.CASCADE)

# class Viewer(models.Model):
#     pass

