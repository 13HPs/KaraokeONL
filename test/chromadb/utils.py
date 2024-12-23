def query_all_collections_with_comparison(query, artists_collection, musics_collection, lyrics_collection, n_results=10):
    # Query all collections
    artist_results = artists_collection.query(query_texts=[query], n_results=n_results)
    music_results = musics_collection.query(query_texts=[query], n_results=n_results)
    lyric_results = lyrics_collection.query(query_texts=[query], n_results=n_results)

    # Extract highest similarity scores
    artist_max_similarity = min(artist_results["distances"][0]) if artist_results["distances"][0] else float('inf')
    music_max_similarity = min(music_results["distances"][0]) if music_results["distances"][0] else float('inf')
    lyric_max_similarity = min(lyric_results["distances"][0]) if lyric_results["distances"][0] else float('inf')

    # Determine the most relevant collection
    collection_scores = {
        "artists": artist_max_similarity,
        "musics": music_max_similarity,
        "lyrics": lyric_max_similarity
    }
    most_relevant_collection = min(collection_scores, key=collection_scores.get)

    if most_relevant_collection == "artists":
        return {"most_relevant": "artists", "results": artist_results}
    elif most_relevant_collection == "musics":
        return {"most_relevant": "musics", "results": music_results}
    elif most_relevant_collection == "lyrics":
        return {"most_relevant": "lyrics", "results": lyric_results}


def extract_lyrics_details(results):
    """
    Extract lyric content, music_id, and lyric order from results.

    Args:
        results (dict): The results dictionary containing lyrics information.

    Returns:
        list: A list of dictionaries with lyric content, music_id, and order.
    """
    # Ensure there is metadata and documents in results
    if not results.get("metadatas") or not results.get("documents"):
        return []

    # Extract data from metadata and documents
    return [
        {
            "lyric_content": document,
            "music_id": metadata["music_id"],
            "lyric_order": metadata["order"],
            "distance": distance
        }
        for metadata, document, distance in zip(results["metadatas"][0],
                                                results["documents"][0],
                                                results["distances"][0],
                                                )
    ]


def extract_artists_details(results):
    """
    Extract artist content including artist name and id from results.

    Args:
        results (dict): The results dictionary containing lyrics information.

    Returns:
        list: A list of dictionaries with artist name and id.
    """
    # Ensure there is metadata and documents in results
    if not results.get("metadatas") or not results.get("documents"):
        return []
    # Extract data from metadata and documents
    return [
        {
            "name": document,
            "artist_id": artist_id,
            "distance": distance
        }
        for artist_id, document, distance in zip(results["ids"][0],
                                                 results["documents"][0],
                                                 results["distances"][0]
                                                 )
    ]


def extract_musics_details(results):
    """
    Extract music content including music name and id from results.

    Args:
        results (dict): The results dictionary containing lyrics information.

    Returns:
        list: A list of dictionaries with music name and id.
    """
    # Ensure there is metadata and documents in results
    if not results.get("metadatas") or not results.get("documents"):
        return []
    # Extract data from metadata and documents
    return [
        {
            "name": document,
            "music_id": music_id,
            "distance": distance
        }
        for music_id, document, distance in zip(results["ids"][0],
                                                results["documents"][0],
                                                results["distances"][0]
                                                )
    ]

