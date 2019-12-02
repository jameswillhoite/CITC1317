#!/usr/bin/perl

use strict;
use CGI ':standard';

#Create the Form
my $form = new CGI;
#Assign some variables
my ($street, $tax, $phone, @type, $subtot);

$street = $form->param('street');
$phone = $form->param('phone');
@type = $form->param('type');

print $street;
