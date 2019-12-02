#!/usr/bin/perl
# James Willhoite
# Lab 9 Words

use Data::Dumper;

#put all words into lower case
my %words = ();
for ( $i = 0; $i < @ARGV; $i++) {
	 $w = lc($ARGV[$i]);
	 $words{$w} = 0;
}

#Read from stdin as place as array
my @line = <STDIN>;

#gothrough each element
foreach  $l (@line) {
	chomp($l);
	#break apart the string by spaces
	 @exp = split (' ', $l);
	foreach my $e (@exp) {
#convert to lowercase
		$e = lc($e);
#remove punctuation
		$e =~ s/[[:punct:]]//g;
		if (exists  $words{$e}) {
			$value = $words{$e};
			 $words{$e} = $value + 1;
		}
	}
}

#Print out the Hash and put in desc order by value then key
foreach (sort { ($words{$b} cmp $words{$a}) || ($a cmp $b) } keys %words) {
	$value = $words{$_};
	print "$_:$value \n";
}


exit();

