	Iozone: Performance Test of File I/O
	        Version $Revision: 3.408 $
		Compiled for 64 bit mode.
		Build: linux 

	Contributors:William Norcott, Don Capps, Isom Crawford, Kirby Collins
	             Al Slater, Scott Rhine, Mike Wisner, Ken Goss
	             Steve Landherr, Brad Smith, Mark Kelly, Dr. Alain CYR,
	             Randy Dunlap, Mark Montague, Dan Million, Gavin Brebner,
	             Jean-Marc Zucconi, Jeff Blomberg, Benny Halevy, Dave Boone,
	             Erik Habbinga, Kris Strecker, Walter Wong, Joshua Root,
	             Fabrice Bacchella, Zhenghua Xue, Qin Li, Darren Sawyer.
	             Ben England.

	Run began: Tue Jan  7 16:56:01 2014

	Record Size 64 KB
	File size set to 409600 KB
	Include fsync in write timing
	Include close in write timing
	Purge Mode On
	Disrupted read patterns selected.
	Command line used: iozone -i0 -i2 -i5 -i8 -r 64k -s 400m -f /tmp/iozone.tmp -ecp -K
	Output is in Kbytes/sec
	Time Resolution = 0.000001 seconds.
	Processor cache size set to 1024 Kbytes.
	Processor cache line size set to 32 bytes.
	File stride size set to 17 * record size.
                                                            random  random    bkwd   record   stride                                   
              KB  reclen   write rewrite    read    reread    read   write    read  rewrite     read   fwrite frewrite   fread  freread
          409600      64   31782   22524                    816017   10411                  3779260                                  

iozone test complete.
