# Search-Engine
A search engine takes a given search phrase or word and finds pages on the internet that are relevant, ranks the pages, and then displays the pages in the order of ranking.

All article metadata can be fetched by calling the wiki.article_metadata(). It returns a 2D list where each individual "row" represents a single article. Each article is represented as a list with the following information provided in this exact order:

Article title (string)

Author name (string)

Timestamp of when the article was published (int). The timestamp is stored as the # of seconds since January 1st, 1970 (also known as Unix/Epoch Time)

The number of characters in the article (int)

A list of keywords that are related to the article content (list of strings)


Preprocessing

In order to help run different searches, there are two pre-processing functions you must implement: title_to_info(metadata) and keyword_to_titles(metadata), both of which take an entire 2D list of article metadata as arguments. As a reminder, each article’s metadata contains [title, author, timestamp, article length, keywords] in that order. The functions reorganize the data into dictionaries to make other search functions easier:

title_to_info - processes article metadata into a dictionary mapping an article title to its metadata, which is in turn a dictionary with the following keys: author, timestamp, and length.

keyword_to_titles - processes article metadata into a dictionary mapping a keyword to a list of all articles containing that keyword.

Basic Search

To run a basic search, ask the user for a keyword and use the keyword to find all article titles relevant to the keyword. For each article, include it in the search results if the user keyword is a (case-sensitive) match for one of the words in the article's relevant keywords list. For example, given the example article above ("Spongebob - the legacy"), it would be included in the search result if the user keyword was "Spongebob" or "tv" but excluded if the user keyword was "bob", "spongebob", or "TV". The function should return a 1D list of article titles where a match was found (note that this is different behavior from the basic search in part 2). To ease this search, it will take in the results from one of your preprocessing steps as an argument.

If the user does not enter anything or no results are found, return an empty list.

When running a search, the basic search will always be run, and it will always be run before the advanced search.

Advanced Search

The user is then prompted for different options to perform an advanced search. There will be 6 advanced search options:

Article title length - user provides a max article title length (in characters). Return a list of article titles from the basic search that do not exceed the max article length.

Key by author - returns a dictionary that remaps the articles from the basic search using authors as the key. The values are a list of all article titles written by that author.

Filter to author - user provides an author. Return the articles from the basic search written by that author.

Filter out - user provides another keyword. Return a list of article titles from the basic search that do not have the new keyword in their "related keywords".

Article year - user provides a year. Return a list of article titles from the basic search that were written in that year.

None - user does not want an advanced search. (There is no function for this)

