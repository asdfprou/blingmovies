import httplib
import string
import urllib
def main():
  conn = httplib.HTTPConnection("www.omdbapi.com")
  results = []

  input_file = open('top250.csv', 'r')
  movies = input_file.read().split('|')
  movie_number = 0

  for movie in movies:
    encoded_movie_title = urllib.quote_plus(movie)
    conn.request("GET", "/?t=" + encoded_movie_title)
    r1 = conn.getresponse()
    response_result = r1.read()
    if '"Response":"False"' not in response_result:
      results.append(response_result)
    movie_number += 1
    if movie_number%10 == 0:
      print movie_number

  # write results together
  results_file = open('results.txt', 'w')
  results_file.write(str(results))
  results_file.close()

main()
