# osu-api.py
[![CodeFactor](https://www.codefactor.io/repository/github/lostpy/osu-api.py/badge)](https://www.codefactor.io/repository/github/lostpy/osu-api.py)  
 A small module to get informations with osu!api

## Index
 1. [Global informations](#globalInfos)

 2. [Installation](#installation)

 3. [Get api key](#getApiKey)
    * [Terms of Use](#termsOfUse)

 4. [Documentation](#documentation)
    * [osu!api V1](#apiV1)
      * [get_beatmaps](#getBeatmaps)
      * [get_user](#getUser)
      * [get_scores](#getScores)
      * [get_user_best](#getUserBest)
      * [get_user_recent](#getUserRecent)
      * [get_match](#getMatch)
      * [get_replay](#getReplay)

    * [osu!api V2](#apiV2)

    * [Enumerate](#enumerate)

## Global informations <a id="globalInfos"></a>
 * Author: [LostPy][me]

 * Version: 1.0
 
 * License: [MIT License][license]

 * Requirements:
   * **Mandatory**
     * [Python 3.x][py]
     * [requests][req]

   * **Optionnal**
     * [pandas][pd]

 * Api supported:
   * [osu!api V1][apiv1]: YES
   * [osu!api V2][apiv2]: Coming soon

 * Utility link:
   * [get a key][api-key]
   * [term of use for osu!api][terms]
   * [osu!api V1][apiv1]
   * [osu!api V2][apiv2]


## Installation <a id="Installation"></a>
To install this package, you can use the following command:

`pip install git+https://github.com/LostPy/osu-api.py.git@main`


**To update** the package, you can use:  
`pip install git+https://github.com/LostPy/osu-api.py.git@main --upgrade`

OR

`pip install git+https://github.com/LostPy/osu-api.py.git@main -U`


## Get a api key <a id="getApiKey"></a>

To get a api key, you can ask [here][api-key].
Before begining, check the [terms of use][terms] of osu!api.

### Terms of use <a id="termsOfUse"></a>
The [terms of use][terms] of osu!api are:

> Use the API for good. Don't overdo it. If in doubt, ask before (ab)using :). this section may expand as necessary.

> Current rate limit is set at an insanely high 1200 requests per minute, with burst capability of up to 200 beyond that. If you require more, you probably fall into the above category of abuse. If you are doing more than 60 requests a minute, you should probably give peppy a yell.

## Documentation <a id="documentation"></a>
This documentation is structured by osu!api

## osu!api V1 <a id="apiV1"></a>

### get_beatmaps <a id="getBeatmaps"></a>
 * **Description:** Function to get general beatmap information.

 * **Arguments:** For more information, check [osu!api][apiv1].
 
 Name | Type | Description | Default value
 ---- |:----:| ----------- |:-------------:
 `key` | *str* | The [api key][api-key] to access at [osu!api][apiv1]. |
 `since` | *str* | To return all beatmaps ranked or loved since this date. Must be a MySQL date. In UTC. | None (return all)
 `beatmapset_id` |*int* | id of beatmapset to return. | None (return all)
 `beatmap_id` |*int* | id of beatmap to return. | None (return all)
 `user` | *int* or *str* | user id or username to return metadata from | None
 `type_` | *str* | `id` or `string` to specify user type. By default, it's automatic recognition. | None
 `mode` | *int* | Mode of beatmaps to return. | None (all game mode)
 `a` | *int* | `0` or `1`. Specify whether converted beatmaps are included (0 = not included, 1 = included). | 0
 `h` | *str* | The beatmap hash. For more info: [osu!api][apiv1] | None
 `limit` | *int* | Amount of results. | 500
 `mods` | *int* | mods that applies to the beatmap requested. You can use the dictionnaty `mods` to get the id of mods | 0 (all mods)
 `type_return` | *str* | The type to return. Take 3 possibles values: `dict`, `json`, `dataframe`. To `dataframe`, the pandas package must be installed. | 'dict'
 
 * **Return:** The result of http request with the data form specify with `type_return`.

### get_user <a id="getUser"></a>
 * **Description:** Function to get general user information.

 * **Arguments:** For more information, check [osu!api][apiv1].
 
 Name | Type | Description | Default value
 ---- |:----:| ----------- |:-------------:
 `key` | *str* | The [api key][api-key] to access at [osu!api][apiv1]. |
 `user` | *int* or *str* | user id or username to return metadata from |
 `type_` | *str* | `id` or `string` to specify user type. By default, it's automatic recognition. | None
 `mode` | *int* | Mode of beatmaps to return. | 0
 `event_days` | *int* | Max number of days between now and last event date. Range of 1-31. | 1
 `type_return` | *str* | The type to return. Take 3 possibles values: `dict`, `json`, `dataframe`. To `dataframe`, the pandas package must be installed. | 'dict'
 
 * **Return:** The result of http request with the data form specify with `type_return`.

### get_scores <a id="getScores"></a>
 * **Description:** Function to get information about the top 100 of a beatmap.

 * **Arguments:** For more information, check [osu!api][apiv1].

 Name | Type | Description | Default value
 ---- |:----:| ----------- |:-------------:
 `key` | *str* | The [api key][api-key] to access at [osu!api][apiv1]. |
 `beatmap_id` |*int* | id of beatmap. |
 `user` | *int* or *str* | user id or username to return metadata from | None
 `type_` | *str* | `id` or `string` to specify user type. By default, it's automatic recognition. | None
 `mode` | *int* | Mode of beatmaps to return. | 0
 `mods` | *int* | mods that applies to the score requested. You can use the dictionnaty `mods` to get the id of mods | 0 (all mods)
 `limit` | *int* | Amount of results. Between 1 & 100 | 50
 `type_return` | *str* | The type to return. Take 3 possibles values: `dict`, `json`, `dataframe`. To `dataframe`, the pandas package must be installed. | 'dict'
 
 * **Return:** The result of http request with the data form specify with `type_return`.

### get_user_best <a id="getUserBest"></a>
 * **Description:** Function to get general user information.

 * **Arguments:** For more information, check [osu!api][apiv1].

 Name | Type | Description | Default value
 ---- |:----:| ----------- |:-------------:
 `key` | *str* | The [api key][api-key] to access at [osu!api][apiv1]. |
 `user` | *int* or *str* | user id or username to return metadata from |
 `mode` | *int* | Mode of beatmaps to return. | 0
 `limit` | *int* | Amount of results. Between 1 & 100 | 10
 `type_` | *str* | `id` or `string` to specify user type. By default, it's automatic recognition. | None
 `type_return` | *str* | The type to return. Take 3 possibles values: `dict`, `json`, `dataframe`. To `dataframe`, the pandas package must be installed. | 'dict'
 
 * **Return:** The result of http request with the data form specify with `type_return`.

### get_user_recent <a id="getUserRecent"></a>
 * **Description:** Function to gets the user's ten most recent plays over the last 24 hours.

 * **Arguments:** For more information, check [osu!api][apiv1].

 Name | Type | Description | Default value
 ---- |:----:| ----------- |:-------------:
 `key` | *str* | The [api key][api-key] to access at [osu!api][apiv1]. |
 `user` | *int* or *str* | user id or username to return metadata from |
 `mode` | *int* | Mode of beatmaps to return. | 0
 `limit` | *int* | Amount of results. Between 1 & 50 | 10
 `type_` | *str* | `id` or `string` to specify user type. By default, it's automatic recognition. | None
 `type_return` | *str* | The type to return. Take 3 possibles values: `dict`, `json`, `dataframe`. To `dataframe`, the pandas package must be installed. | 'dict'
 
 * **Return:** The result of http request with the data form specify with `type_return`.

### get_match <a id="getMatch"></a>
 * **Description:** Function to gets information about multiplayer match.

 * **Arguments:** For more information, check [osu!api][apiv1].

 Name | Type | Description | Default value
 ---- |:----:| ----------- |:-------------:
 `key` | *str* | The [api key][api-key] to access at [osu!api][apiv1]. |
 `match_id` | *int* | Id of match to return. |
 `type_return` | *str* | The type to return. Take 3 possibles values: `dict`, `json`, `dataframe`. To `dataframe`, the pandas package must be installed. | 'dict'
 
 * **Return:** The result of http request with the data form specify with `type_return`.

### get_replay <a id="getReplay"></a>
 * **Description:** Function to gets the user's ten most recent plays over the last 24 hours.

 * **Arguments:** For more information, check [osu!api][apiv1].

 Name | Type | Description | Default value
 ---- |:----:| ----------- |:-------------:
 `key` | *str* | The [api key][api-key] to access at [osu!api][apiv1]. |
 `beatmap_id` |*int* | id of beatmap. |
 `user` | *int* or *str* | user id or username to return metadata from |
 `mode` | *int* | Mode of beatmaps to return. | None
 `score_id` | *int* | id of score to return. May be passed instead of `b` and `u`. | None
 `type_` | *str* | `id` or `string` to specify user type. By default, it's automatic recognition. | None
 `mods` | *int* | mod or mods combination. You can use the dictionnaty `mods` to get the id of mods. | None
 
 * **Return:** The result of http request with the data form specify with `type_return`.

## osu!api V2 <a id="apiV2"></a>
Coming soon...


## Enumerate <a id="Enumerate"></a>
Coming soon...


## Index
 1. [Global informations](#globalInfos)

 2. [Installation](#installation)

 3. [Get api key](#getApiKey)
    * [Terms of Use](#termsOfUse)

 4. [Documentation](#documentation)
    * [osu!api V1](#apiV1)
      * [get_beatmaps](#getBeatmaps)
      * [get_user](#getUser)
      * [get_scores](#getScores)
      * [get_user_best](#getUserBest)
      * [get_user_recent](#getUserRecent)
      * [get_match](#getMatch)
      * [get_replay](#getReplay)

    * [osu!api V2](#apiV2)

    * [Enumerate](#enumerate)


[py]: https://www.python.org/
[req]: https://requests.readthedocs.io/en/master/
[pd]: https://pandas.pydata.org/
[apiv1]: https://github.com/ppy/osu-api/wiki
[apiv2]: https://osu.ppy.sh/docs/index.html
[terms]: https://osu.ppy.sh/docs/index.html#terms-of-use
[api-key]: https://osu.ppy.sh/p/api/
[license]: https://github.com/LostPy/osu-api.py/blob/main/LICENSE
[me]: https://osu.ppy.sh/users/11187592