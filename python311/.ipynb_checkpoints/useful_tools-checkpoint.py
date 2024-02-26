{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a4790785-c806-4b06-ab24-990cadf60d7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# MODULES AND PIP\n",
    "import random\n",
    "\n",
    "feet_in_mile = 5280\n",
    "meters_in_kilometer = 1000\n",
    "beatles = [\"John Lennon\", \"Paul McCartney\", \"Ringo\", \"Starr\", \"George Harrison\"]\n",
    "\n",
    "def get_file_ext(filename):\n",
    "    return filename[filename.index(\".\") + 1:]\n",
    "\n",
    "def roll_dice(num):\n",
    "    return random.randint(1,num)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
