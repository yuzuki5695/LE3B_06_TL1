

# オペレータ 出現ポイントの
class SpawnNames():

    # インデックス
    PROTOTYPE = 0   # プロトタイプのオブジェクト名
    INSTANCE = 1    # 量産時のオブジェクト名
    FILENAME = 2    # リソースファイル名

    names = {}
    # names["キー"] = (プロトタイプのオブジェクト名, 量産時のオブジェクト名, リソースファイル名)
    names["Enemy"] = ("PrototypeEnemySpawn", "EnemySpawn", "enemy/Enemy.obj")
    names["Player"] = ("PrototypePlayerSpawn", "PlayerSpawn", "player/player.obj")