
require 'net/http'

Net::HTTP.start 'www.pythonchallenge.com' do |http|
  nothing = 90033
  while (text = http.get("/pc/def/linkedlist.php?nothing=#{nothing}").body)
    puts text
    case text
        when /(\d+)$/ then nothing=$1.to_i
        when /by two/ then nothing=nothing / 2
        when /\.html/ then puts $`; break;
    end
  end
end