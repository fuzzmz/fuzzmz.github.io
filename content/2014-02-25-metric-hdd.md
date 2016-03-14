title: Get your metric prefix out of my base 2
date: 2014-02-25
slug: metric-hdd
category: misc
tags: storage, maths
summary: I got myself a really nice Samsung SSD to replace the slow as hell 5400RPM WD I had as my main drive in my laptop, and seeing the size got me to thinking about base conversion. Let's do conversions!

![featureimage](/images/metric-hdd/samsung_ssd.jpg)

I got myself a really nice Samsung SSD to replace the slow as hell 5400RPM WD I had as my main drive in my laptop, and seeing the size got me to thinking about base conversion.

Let's do conversions!
<div class="container">
<blockquote>"Real hardware works in base two, hard drive marketing fluff in base 10. That's all the context knowledge you need."</blockquote>
<div class="reference">
<strong>Some people say...</strong>
<p>Now ain't that cute? But it's wrong!</p>
</div>
</div>

There is nothing in a hard drive that requires or even encourages capacity to come in powers of two. Heck, they don't even have to have an even number of platters, or of active surfaces. Nor a power-of-two related number of cylinders, or number of sectors per track. The latter figure in fact varies from outer cylinder to inner. I am currently looking at a "4 TB" hard drive, or rather a 4 TB partition, which occupies the entire drive. Windows reports this as 4,000,650,883,072 bytes. Which power of 1024 would you prefer be used? 3.63 TiB, or 3725.9 GiB?

Yes, the sectors are 512, now 4096, bytes each, but there's really nothing in a hard drive that requires that either. 512 bytes is a legacy of early virtual memory operating systems that ran on hardware that used 512 byte pages; making your sector size the same as your page size is convenient. And making that a power of two is convenient for building DMA controllers that talk to the hard drive; you don't have to implement the low-order 9 bits of memory address or transfer length.

There are numerous other examples in hardware storage capacity. The most obvious is a tape cartridge. The tape is generally as long as it can be and still fit in the cart. Its capacity is whatever fits on that length of tape. An LTO-4 cart has a native capacity of a little more than 800,000,000,000 bytes. There is nothing about it that encourages a capacity that's related to a power of 1024. Or of 2, for that matter.

The same is true of clock rates: A CPU clocked at "2 GHz" is clocked at 2,000,000,000 Hz. Really. A NIC running at "100 megabits/sec" is running at 100,000,000 bits/sec. And so on.

 But there's also RAM!

RAM is different. Because of the way it's addressed, it is very convenient that the chips (and therefore DIMMs) have sizes that can be expressed as binary numbers with a whole lot of trailing zeroes. If you had 28 bits of address coming into a DIMM, but the DIMM only implemented 250,000,000 bytes instead of 268,435,456, then something in the system would have to keep track of which combinations of address bits weren't really implemented in that DIMM. As it is, it is easy for multiple DIMMs to be aggregated into a single array that presents one block of physically contiguous addresses to the CPU.

In this, RAM is the exception, not the rule. Darn little else in computing has any technical reason for coming in "binary megabytes" or "binary gigabytes".

I would also add that hard drives have always been marked in powers-of-1000 capacities, going back to the original IBM RAMAC drive (capacity of 5 million characters, having 50 surfaces with a capacity of 100,000 characters each). At that time memory was expressed in "KB", which meant 1024 bytes, this being subtly distinguishable—if everyone was paying attention and whoever prepared the written materials didn't "correct" things—from "kB", which meant 1000 bytes, the way SI intended.

Unfortunately the SI prefixes for mega, giga, and tera were already uppercased; m already meant "milli", etc. Nevertheless the main memory makers, who of course got to the "mega" range many many years after the hard drives did, just went ahead and co-opted the M prefix to mean 1024² even though the hard drive makers were already using it in its proper SI meaning. And repeat for giga and tera. It's the RAM makers who ignored the standards.
