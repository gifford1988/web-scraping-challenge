{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, jsonify, redirect\n",
    "from flask_pymongo import PyMongo\n",
    "import scrape_mars\n",
    "\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "\n",
    "mongo = PyMongo(app)\n",
    "\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    mars = mongo.db.mars.find_one()\n",
    "    return render_template('index.html', mars=mars)\n",
    "\n",
    "\n",
    "@app.route('/scrape')\n",
    "def scrape():\n",
    "    mars = mongo.db.mars\n",
    "    #print(mars)\n",
    "    data = scrape_mars.scrape()\n",
    "    print(data)\n",
    "    mars.update(\n",
    "        {},\n",
    "        data,\n",
    "        upsert=True\n",
    "    )\n",
    "    return redirect('/', code=302)\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
