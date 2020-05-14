from requests import request
from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return HttpResponse('''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	 <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">


    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>


    <title>Home</title>

      <style>
          {% block css %}
				body{
    background-image: url('D:\p\Another\mysite\patient\static\patient\853644-gorgerous-green-l.jpg') ;
    background-size:cover;
    background-repeat: no-repeat;
    background-position: center;
    background-attachment: fixed;
}
           {% endblock %}
      </style>

  </head>
  <body style="font-family: Arial, Helvetica, sans-serif;">

    <!-- Top Logo and Heading -->
			<!-- Top Logo and Heading -->
	<div class="container-fluid text-white"
		style="background-image: linear-gradient(to right,#000000 , #132b08, #19420e, #1d5a13);">
		<div class="row">
			<div class="col-xl-2 col-lg-2 col-md-3 col-sm-12 col-12 text-sm-center text-center">
				<a href="{% url 'p_Home' %}"><img src="D:\p\Another\mysite\patient\static\patient\logo.png" class="" style="height: 150px;  box-shadow: 10px 5px 10px black;"></a>
			</div>
			<div
				class="col-xl-5 col-lg-5 col-md-4 col-sm-12 col-12">
				<h3 class="text-white text-sm-center text-center text-md-left mt-lg-5 mt-md-5 mt-xl-5 pt-lg-4 pt-xl-4 pt-md-4" style="text-align: left; letter-spacing: 3px; font-size: 50px;">Naturopath</h3>
			</div>

			<div
				class="col-xl-5 col-lg-5 col-md-5 col-sm-12 col-12 align-bottom mt-md-4">
				<h4 class="text-white text-xl-right text-lg-center text-md-right text-md-right text-sm-center text-center mt-2 mt-lg-5 mt-md-5 mt-xl-5 pt-lg-4 pt-xl-4 pt-md-4 " style="font-size: 2vw" >Rejuvenate Mind and Body</h4>
			</div>

		</div>

    </div>

    <div class="container mt-4 mb-4 m-auto">

        <div class="row mt-5 mb-5">
            <div class='col-12 col-sm-12 col-md-6 col-lg-6 col-xl-6 '>

                <a href='{% url "/patient/" %}'> Patient</a>

            </div>
            <div class="col-12 col-sm-12 col-md-6 col-lg-6 col-xl-6 " >

                <a href='{% url "/doctor/" %}'> Doctor</a>

            </div>

        </div>

    </div>
    




	<footer class="container-fluid pl-0 pr-0">
			<div class="mt-5 p-5 bg-dark text-light text-center">
				<small>&copy; Copyright 2020, NASS Corporation</small>
				<br>
				<p style="word-spacing: 10px; letter-spacing: 3px;">@Ankit   @NItish   @Suchismita   @Subhasmita</p>
			</div>

		</footer>

  </body>
</html>

     ''')

    # return render(request, 'mysite/home.html')
