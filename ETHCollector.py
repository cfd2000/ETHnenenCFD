B
    �!]�  �            	   @   s�  d dl Z d dlZd dlZd dlZd dlZd dlmZ d dlmZ d dlm	Z	m
Z
mZ ejdd� eje	j d ej e	j d ej e	j d	 ej e	j d
 ej d ej e	j d ej e	j d ej d ej e	j d Zee� eje	j ZejZeje	j Zeje	j Zeje	j Zeje	j Zeje	j Zeje	j Ze � � Z!dd� Z"e#dd��Z$e$�%� Z&W dQ R X e�'e&�Z(e(d Z)e(d Z*ddiZ+e,ed e d e �Z-e-ddddd�Z&ye!j.e)e+e&d�Z/W n    eed  � e�0�  Y nX ee/j1d!�Z2e2j3d"d#d$�Z4xPe4D ]HZ5ej6�7ed% � ed&� ej6�7ed' e d( e e5j8 e d) � �qW eed* e d+ � �x^x�e9d,�D ]�Z:e:d-7 Z:y�e!j.e*e+d.e:ie/j;d/� e!j.e*e+d0e:ie/j;d/�Z<e<j8d1k�r�eed2 e e=e:� e d3 � n2eed4 e e=e:� e d5 e e<j8 e d6 � W n,   eed7 e e=e:� � ed8� Y nX �q�W e!j>e)e+e/j;d9�Z?ee?j1d!�Z2e2j3d"d#d$�Z4xDe4D ]<Z5eed: e e d; e d< ee5j8 ed= e d> � �q�W e"d?� �qxW dS )@�    N)�BeautifulSoup)�sleep)�Fore�Back�StyleT)Z	autoresetz�       __       _       __
      / /__    (_)___ _/ /______ _
 __  / / _ \  / / __ `/ //_/ __ `/
/ /_/ /  __/ / / /_/ / ,< / /_/ /
\____/\___/_/ /\__,_/_/|_|\__,_/                                            /___/
z:=========================================================
zAuthor By  z :z	 Kadal15
z
Channel Ytz  : zJejaka Tutorial
z,Bot Auto Claim APK Sejenis ETH Collector Dllc             C   sn   t j�d� t j�d� xDt| dd�D ]4}t j�d� t j�d�|�� t j��  td� q&W t j�d� d S )N�z?                                                               r   �����z,[1;30m#[1;0m{:2d} [1;32mseconds remaining�   z+                                         )�sys�stdout�write�range�format�flushr   )�x�	remaining� r   �	ethcol.py�tunggu    s    
r   zurl.json�rZIndexZAjaxz
User-Agentz�Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36zEnter Your Wallet z: ZID29301zim notZLogin�1)ZwalletZrefbyZbotprotectionZsubmitZsubmit_address)�headers�datazLogin Time Out Please Try Againzhtml.parserZdivzwidget-int num-count)Zclass_zLogin�   zYour Ballancez         : z Point
z

Start Claiming z....!�   r	   Zreset_contest_button)r   r   �cookiesZ confirm_exploaration_point_claim�0zButton z Alredy Claimed..!zSuccess To Claim Button z = z PointzFiled To Claim Button �   )r   r   z////zChecking Balance �:ZPointz/////i,  )@Zrequestsr
   �osZcoloramaZjsonZbs4r   �timer   r   r   r   �initZNORMALZMAGENTAZGREENZBRIGHTZDIMZWHITEZ	RESET_ALLZbanner�printZhijau�resZabu2ZunguZhijau2ZYELLOWZyellow2ZREDZred2ZredZSession�cr   �openZmyfile�readr   �loads�obj�indexZajaxZua�inputZwaletZpostr   �exit�contentZsoupZfind_allZballZballancer   r   �textr   �ir   Zr1�str�getZr2r   r   r   r   �<module>   sv   (�

0"6
<