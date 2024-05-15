import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json
import pymongo
from pprint import pprint
from bson.objectid import ObjectId

darks ="""\033[95m
██╗      █████╗ ███████╗██╗   ██╗██████╗  █████╗ ██████╗ ██╗  ██╗
██║     ██╔══██╗╚══███╔╝╚██╗ ██╔╝██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝
██║     ███████║  ███╔╝  ╚████╔╝ ██║  ██║███████║██████╔╝█████╔╝
██║     ██╔══██║ ███╔╝    ╚██╔╝  ██║  ██║██╔══██║██╔══██╗██╔═██╗
███████╗██║  ██║███████╗   ██║   ██████╔╝██║  ██║██║  ██║██║  ██╗
╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
\033[0m \033[92m@payperme\033[0m"""
print(darks)
parser = argparse.ArgumentParser(description="navigate into dark")
parser.add_argument('-u', '--url', type=str, help='tor url')
parser.add_argument('-l', '--list', type=str, help='list url file')
parser.add_argument('-s', '--search', type=str, help='Search in documents')
parser.add_argument('-d', '--delete', type=str, help='Object ID')

args = parser.parse_args()

def jff(linx, tlts, arls=None):
    urls_doc = {}
    urls_doc['url'] = linx
    urls_doc['title'] = tlts
    if arls is not None:
        urls_doc['links'] = arls
    urls_json = json.dumps(urls_doc, indent=4)
    insertMango(urls_doc)
    print(urls_json)

def insertMango(jsonFormat):
    collection = mongol()
    print("Connected to Mongolica Database")
    collection.insert_one(jsonFormat)
    print("Document inserted successfully")

def searchMango(search_term):
    collection = mongol()
    print("Connected to Mongolica Database")
    query = {"$or": [{"url": {"$regex": search_term, "$options": "i"}},
                     {"title": {"$regex": search_term, "$options": "i"}},
                     {"links": {"$regex": search_term, "$options": "i"}}]}
    results = collection.find(query)
    for result in results:
        pprint(result)

def deleteMango(objectID):
    collection = mongol()
    print("Connected to Mongolica Database")
    result = collection.delete_one({'_id': ObjectId(objectID)})
    if result.deleted_count == 1:
        print(f"Document with _id '{objectID}' deleted successfully.")
    else:
        print(f"No document found with _id '{objectID}'.")

def mongol():
    try:
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['dark']
        collection = db['scrap']
        return collection
        #collection.insert_one(jsonFormat)
        #print("Document inserted successfully.")
    except pymongo.errors.ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")
    except pymongo.errors.ServerSelectionTimeoutError as e:
        print(f"Error: Server selection timeout: {e}")
    except pymongo.errors.PyMongoError as e:
        print(f"PyMongo error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        client.close()

if args.url:
    urlpas = urlparse(args.url)
    if urlpas.scheme not in ('http', 'https'):
        args.url = f"http://{args.url}"
    try:
        response = requests.get(args.url)
        if response.status_code != 404:
            soup = BeautifulSoup(response.text, 'lxml')
            title_tag = soup.title
            if title_tag:
                title_content = title_tag.string
            else:
                title_content = 'no title'
            #urls_doc = {}
            urls_in = []
            if len(soup.find_all('a')) != 0:
                for a in soup.find_all('a'):
                    urls_in.append(a['href'])
                jff(args.url, title_content, urls_in)
            else:
                jff(args.url, title_content)
        else:
            print(f"Error: URL '{args.url}' Offline")
    except Exception as e:
        print(f"Error: {e}")

if args.search:
    searchMango(args.search)

if args.delete:
    deleteMango(args.delete)
