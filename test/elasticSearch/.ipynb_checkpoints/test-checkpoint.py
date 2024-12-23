from elasticsearch import Elasticsearch

es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, 'scheme': 'http'}],
    http_auth=('elastic', '8fz0_sdwWvM265nx0mZH')
)
print(es.ping())
index_name = 'musics'
for i in range(1, 11):
    music_doc = {
        'id': "123",
        'name': f'Song {i}',
        'artists': [f'Artist {i}', f'Artist {i+1}'],
        'genres': [f'Genre {i}', f'Genre {i+1}', f'Genre {i+2}'],
        'music_url': f'https://music.com/song{i}',
       'metric_url': f'https://metrics.com/song{i}_metric.json',
        'lyrics': [f'Lyric {i}', f'Lyric {i+1}', f'Lyric {i+2}']
    }
    try:
        if es.ping():
            print("Connected to Elasticsearch!")
            index_name = "test_index"
            for i in range(3):  # Create multiple indices as an example
                response = es.indices.create(index=index_name + "_" + str(i))
                print(f"Index {index_name}_{i} created:", response)
        else:
            print("Elasticsearch is not responding.")
    except Exception as e:
        print("Error:", str(e))
