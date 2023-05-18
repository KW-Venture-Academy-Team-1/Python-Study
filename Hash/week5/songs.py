def solution(genres, plays):
    # 장르별 총 재생 수와 (index, 재생 수) 정보를 담은 리스트를 저장할 딕셔너리
    genre_play_count = {}
    # 각 곡의 고유 번호와 (장르, 재생 수) 정보를 담은 리스트를 저장할 리스트
    song_info = []

    # 장르별 총 재생 수와 (index, 재생 수) 정보를 담은 리스트를 만듦
    for i in range(len(genres)):
        if genres[i] in genre_play_count:
            genre_play_count[genres[i]] += plays[i]
        else:
            genre_play_count[genres[i]] = plays[i]
        song_info.append((i, genres[i], plays[i]))

    # 장르별 총 재생 수를 기준으로 내림차순 정렬
    sorted_genre_play_count = sorted(genre_play_count.items(), key=lambda x: x[1], reverse=True)

    answer = []
    # 장르별로 노래를 선택
    for genre, _ in sorted_genre_play_count:
        # 선택된 장르의 노래 정보를 추출하여 재생 수를 기준으로 내림차순 정렬
        genre_song_info = [info for info in song_info if info[1] == genre]
        sorted_genre_song_info = sorted(genre_song_info, key=lambda x: x[2], reverse=True)

        # 장르 내에서 최대 2곡 선택
        for i in range(min(len(sorted_genre_song_info), 2)):
            answer.append(sorted_genre_song_info[i][0])

    return answer
