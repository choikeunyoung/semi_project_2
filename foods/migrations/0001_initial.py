# Generated by Django 3.2.13 on 2022-11-19 15:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import foods.models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('address', models.TextField()),
                ('lat', models.TextField()),
                ('lon', models.TextField()),
                ('content', models.TextField()),
                ('following_users', models.ManyToManyField(related_name='following_restaurants', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='team_restaurants', to='articles.team')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('grade', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('restaurant_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_reviews', to='foods.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('lat', models.TextField()),
                ('lon', models.TextField()),
                ('items', models.TextField()),
                ('detail', models.TextField()),
                ('following_users', models.ManyToManyField(blank=True, related_name='following_stores', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='team_stores', to='articles.team')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoreImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=foods.models.user_directory_path)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_image', to='foods.store')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_image', to='foods.review')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='store_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='store_reviews', to='foods.store'),
        ),
        migrations.AddField(
            model_name='review',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tag_articles', to='foods.Tag'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='RestaurantImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_image', to='foods.restaurant')),
            ],
        ),
    ]