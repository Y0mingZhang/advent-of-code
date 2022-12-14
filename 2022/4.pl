#!/usr/bin/perl

use strict;
use warnings;

use Path::Tiny;
use List::Util qw( min max );

my $file = path("../data/4.in");

my $fin = $file->openr_utf8();

my $covers = 0;
my $overlaps = 0;

while( my $line = $fin->getline() ) {
        my @fields = split(',', $line);
        my @left = split('-', $fields[0]);
        my @right = split('-', $fields[1]);

        
        if($left[0] <= $right[0] and $left[1] >= $right[1]) {
                $covers += 1;
        } elsif($left[0] >= $right[0] and $left[1] <= $right[1]) {
                $covers += 1;
        }

        if(max($left[0], $right[0]) <= min($left[1], $right[1])) {
                $overlaps += 1;
        }
        
}

print("part1\n", $covers, "\n");
print("part2\n", $overlaps, "\n");
