from django.db import models
from statistics import mean

class User(models.Model):
    wg_user = models.IntegerField(default=0, unique=True)
    name = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

class Nation(models.Model):
    name = models.CharField(max_length=255)
    human_name = models.CharField(max_length=255)

class TankType(models.Model):
    name = models.CharField(max_length=255)

class Tank(models.Model):
    wg_identifier = models.BigIntegerField(default=0, db_index=True)
    name = models.CharField(max_length=200)
    tier = models.IntegerField(default=0)
    playercount = models.IntegerField(default=0)
    average_wr = models.DecimalField(max_digits=6, decimal_places=5, default=0)
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)
    type = models.ForeignKey(TankType, on_delete=models.CASCADE)
    is_premium = models.BooleanField()
    img = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    
    def update(self):
        stats = list(UserStat.objects.filter(tank = self))
        self.playercount = len(stats)
        averagestats = [stat.wins/stat.battles for stat in stats]
        self.average_wr = mean(averagestats)
        self.save()
        
    def get_node(self):
        return {
            "id": self.pk,
            "name": self.name,
            "playercount": self.playercount,
            "nation": self.nation.name
        }
    
    # compare the stats between two tanks and return a least-squares weighted
    # fit between their statistics
    def compare_tank(self, tank2):
        return 0

class UserStat(models.Model):
    wg_user = models.ForeignKey(User, to_field='wg_user', on_delete=models.CASCADE)
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)

    spotted = models.IntegerField(default=0)
    survived_battles = models.IntegerField(default=0)
    hits_percents = models.IntegerField(default=0)
    battles = models.IntegerField(default=0)
    damage_received = models.IntegerField(default=0)
    frags = models.IntegerField(default=0)
    stun_number = models.IntegerField(default=0)
    capture_points = models.IntegerField(default=0)
    hits = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    damage_dealt = models.IntegerField(default=0)
    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['wg_user','tank']),
            models.Index(fields=['tank','wg_user']),
            models.Index(fields=['tank','updated_at']),
        ]

        constraints = [
            models.UniqueConstraint(fields=['wg_user', 'tank'], name='unique_tank_entry'),
        ]
