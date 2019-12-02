#!/usr/bin/perl
# James Willhoite
# Lab 9 Credit Card

$user_input = $ARGV[0];

if(!$user_input) {
	print "Please enter a credit card number: ";
	$user_input = <STDIN>;
}

#Check to make sure that numbers are enter
if ($user_input !~ /^[0-9\s\-]*$/) {
	print "Invalid Card Number";
	exit();
}

#Strip out anything that are not numbers
$user_input =~ s/[^0-9]//g;

#Make sure that the string is 16 characters long
if (length($user_input) ne 16) {
	print "Invalid card number. Must be 16 digits long";
	exit();
}

#now break up the string into 4 groups of 4
@groups = ( $user_input =~ m/..../g );

#now print out the 4 groups of 4
print "Credit card numbers are...\n";
foreach $group (@groups) {
	print($group . "\n");
}

exit();

