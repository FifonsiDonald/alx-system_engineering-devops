#!/usr/bin/env ruby
# script that accepts one argument and passes it to a regexp matching method (School)
puts ARGV[0].scan(/School/).join
