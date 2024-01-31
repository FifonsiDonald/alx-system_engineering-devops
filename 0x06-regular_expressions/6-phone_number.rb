#!/usr/bin/env ruby
# script with regexp to match a 10 digit phone number

puts ARGV[0].scan(/^\d{10}$/).join
