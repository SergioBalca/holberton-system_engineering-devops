#!/usr/bin/env ruby
# regular expression that match hbtn, with t repeted 2,3,4 and 5 times
puts ARGV[0].scan(/hbt{2,5}n/)

