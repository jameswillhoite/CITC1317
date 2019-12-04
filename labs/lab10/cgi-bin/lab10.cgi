#!/usr/bin/perl

use strict;
use CGI ':standard';
use feature qw(switch);

#Create the Form
my $form = new CGI;
#Assign some variables
my ($street, $tax, $phone, @type, $subtotal);
my ($topping);

$street = $form->param('street');
$phone = $form->param('phone');
@type = $form->param('type');


print $form->header;
$form->start_html('Yee Ole\' Ice Cream Shope');

# Validation
if ( ($street eq "") or ($phone eq "") ) {
	print "<strong>Please enter a Street Address and a Phone Number</strong>";
	print $form->end_html;
	exit 0;
}

# Make sure there is no spoofing
for $topping (@type) {
	if (
		$topping ne "Chocolate" and
		$topping ne "Vanilla" and
		$topping ne "Strawberry" and
		$topping ne "Mocha Chip" and
		$topping ne "Coffee Crunch"
	)
	{
		print "Hello, <br/>Thanks for tying to add flavors that don't exist. Please only use the selection boxes on ";
		print "the form from the previous page.<br/>Thanks,<br/>Webmaster.";
		print $form->end_html;
		exit 0;
	}
}

# Make sure the user has selected at least one flavor
if(scalar(@type) == 0) {
	print "<strong>Please select at least one Flavor of Ice Cream. <em>You know you want two....</em></strong>";
	print $form->end_html;
	exit 0;
}

# Print out the Receipt
print "<div style='font-size: 18px;'><strong>Please review your order</strong></div>";
print "<div>Street Address: $street<br/>";
print "Phone: $phone<br/><br/>";
print "Ice Cream selected:<br/>";

#start the subtotal
$subtotal = 0;

for $topping (@type) {
	if (
		$topping eq "Chocolate" or
		$topping eq "Vanilla" or
		$topping eq "Strawberry"
	)
	{
		print "$topping: \$1.25<br/>";
		$subtotal += 1.25;
	}
	else {
		print "$topping: \$1.75<br/>";
		$subtotal += 1.75;
	}
}

print "<br/>";

printf "Subtotal:\$%.2f<br/>", $subtotal;
$tax = $subtotal * 0.0925;
printf "Tax:\$%.2f<br/>", $tax;
printf "<strong>Order Total:\$%.2f</strong><br/>", $tax + $subtotal;
print "</div>";
print $form->end_html;
exit 0;



print $form->end_html;
exit 0;