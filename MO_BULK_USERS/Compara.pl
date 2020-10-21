#!/usr/bin/perl -w	
#Abre archivo1, abre archivo2, si existe un numero del archivo2 que no esta en archivo1 lo guarda en "resultados"
#my $log = "algo.txt";

#exec `echo tail -f $log`;

#pid_log.pl

my %hash;

open FILE1 , '<', 'prefix.txt';

while (<FILE1>)
{
   	$hash{ (split /\t/, $_)[0] } = 1;
}

close FILE1;

open FILE2 , '<', 'sospechoso.txt';
open (OUTPUT, '+>','resultados'); # se modifica >> por +> para reescrbir archivo y no añadir
while (my $linea = <FILE2>)
{
    	if ( not exists $hash{ (split /\t/, $linea)[0] } )
	{
        print OUTPUT $linea;
    	}
}
close OUTPUT;
close FILE2;

END;
