a
    ���`�  �                   @   s�  d dl Z d dlZd dlZd dlZd dlZd dlT dZed� ed� ed� ed� ed� dd	� Z	d
d� Z
G dd� d�Zg Zej�ej�e��Zej�ed�Zee���Ze jedd�Zd ZeD ]FZed kr�ed7 Zq�ed7 Zeed  ed ed ed �Ze�e� q�eded � d�� W d  � n1 �s20    Y  eedd� d�Ze�� Zd Zee�d k�r�ed7 Zej� � ed  jej!ed� k �rej� � ed  jk �r�edej� � � ded  jej� �  �"� d � d�� e�#ed � �q�edej� � � d�� ed  ��  e�#d� ed  j$ej� �  �"� Z%e%d k�rdedej� � � ded  j$� �� e�#e%� ej� � ed  j$k�r�ed ed  j$� �� ed  �&�  e�#d� e�'d � ed!ee�� d"�� ned#� �qXed$� dS )%�    N)�*�   z   AUTOZOOM-BOT� z9                        [*] Developed By Devil Master [*]z9                        [+]     github.com/isuruwa    [+]c                 C   s�   z| � d�d }W n   td| � d��}Y n0 z| � d�d � d�d }W nX   td| � d	��}|d
krpdn|�� }|dkr�td| � d�� ntd|� �� Y n0 z| � d�d � d�d }W n   d
}td� Y n0 |||fS )Nzpwd=r   z[*] PASSWORD z# Not Detected 
[*] Enter Manually 
z/j/z?pwd=r   zConference Code z1 Not Detected . 
Enter Conderence Code Manuaally
r   zNot Detectedz+ Not Detected  
Trying Other Alternatives .zYour Conference Code  is z//z/jzWhere Is Domain ?)�split�input�strip�print)�link�password�conference_code�zoom_domain_name� r   �
zoombot.py�decode_link   s0    
�

�
�r   c                 C   s�   |� d�d }|� d�d }| dkr(d} | dkrTtj�� �d�� d|� d|� d�}nf| d	v r�tj�� }|�d
�| kr�|tjdd� }qf|�d�� d|� d|� d�}n| � d|� d|� d�}tj�|d�}|S )N�:r   r   r   �todayz%m/%d/%y� z:00)ZMondayZTuesdayZ	WednesdayZThursdayZFridayZSaturdayZSundayz%A)Zdaysz%m/%d/%y %H:%M:%S)r   �datetime�dater   �strftime�	timedelta�strptime)Zstring_dateZstring_timeZhourZminuteZdatetime_strZcurdateZdatetime_objectr   r   r   �convert_time)   s    $
r   c                   @   s$   e Zd Zdd� Zdd� Zdd� ZdS )�Meetingc                 C   sd   zt ||�| _t ||�| _W n(   td|� d|� d|� d�� Y n0 t|�\| _| _| _|| _d S )Nz#Meeting DATE or TIME Error Found 
 z 
Time : 
 z - z%. 
Reccomand - Re-edit Time,date [0m)	r   �
start_time�end_timer   r   r   r
   r   r	   )�selfr	   r   r   r   r   r   r   �__init__F   s    �
zMeeting.__init__c                 C   s�   t �� dkrB| jdkr$d| j� �}qxd| j� d| j� d| j� �}n6| jdkrZd| j� �}nd| j� d| j� d	| j� d
�}t�|� d S )N�Windowsz	NOT FOUNDzstart zstart zoommtg://z/join?confno=z?"&"pwd=zopen zopen "zoommtg://z?&pwd=�")�platform�systemr   r	   r   r
   �os)r   Zcommandr   r   r   �joinQ   s    

zMeeting.joinc                 C   s&   t �� dkrt�d� n
t�d� d S )Nr   ztaskkill /f /im Zoom.exezkillall zoom.us)r    r!   r"   )r   r   r   r   �quit^   s    zMeeting.quitN)�__name__�
__module__�__qualname__r   r#   r$   r   r   r   r   r   D   s   r   z
mylist.csv�,)Z	delimiter�   �   z[*] Found :  z
 MEETING 
c                 C   s   | j S )N)r   )�xr   r   r   �<lambda>x   �    r,   )�key)Zminutesz1. Current Meeting : z 
2. Next Meeting : �
   z mins
zCurrent Meeting : z 
Trying To Join Meeting ......z 
Current Meeting Ended On : z[*] Meeting : Existing zFound z More Meetingsz[*] Unknown Error z,Done ! Expect US ! DEVELOPED BY DEVIL MASTER)(Zcsvr"   �timer   r    ZartZLATE_THRESHOLDZtprintr   r   r   r   Zmeeting_list�path�abspath�dirname�__file__Z	file_pathr#   Zcsv_path�openZcsv_file�readerZ
csv_readerZ
line_count�rowZmeeting�append�sortedr   Z
loop_count�lenZnowr   Ztotal_seconds�sleepr   Zmeeting_remaining_timer$   �popr   r   r   r   �<module>   sf   ("

4".��

 


