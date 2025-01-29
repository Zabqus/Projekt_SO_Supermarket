import mmap
import os
import pickle
import select
import struct
import fcntl
import errno


class SharedMemoryQueue:
    def __init__(self):
        self.read_fd, self.write_fd = os.pipe()
        flags = fcntl.fcntl(self.write_fd, fcntl.F_GETFL)
        fcntl.fcntl(self.write_fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)
        '''tworzenie pliku pamięci współdzielonej'''
        self.shm_fd = os.open('/dev/shm/queue_size', os.O_CREAT | os.O_RDWR)
        os.write(self.shm_fd, b'\x00\x00\x00\x00')
        self.size_map = mmap.mmap(self.shm_fd, 4)

    def put(self, item):
        try:
            data = pickle.dumps(item)
            length = struct.pack('!I', len(data))
            written = os.write(self.write_fd, length + data)
            if written > 0:
                self._set_size(self._get_size() + 1)
            return True
        except (OSError, IOError) as e:
            if e.errno == errno.EAGAIN:
                return False
            raise

    def get(self, timeout=None):
        if timeout is not None:
            ready, _, _ = select.select([self.read_fd], [], [], timeout)
            if not ready:
                raise Empty()

        try:
            length_data = os.read(self.read_fd, 4)
            if not length_data or len(length_data) != 4:
                raise Empty()

            length = struct.unpack('!I', length_data)[0]
            data = os.read(self.read_fd, length)
            if len(data) != length:
                raise Empty()

            self._set_size(max(0, self._get_size() - 1))
            return pickle.loads(data)
        except EOFError:
            raise Empty()

    def _get_size(self):
        self.size_map.seek(0)
        return struct.unpack('i', self.size_map.read(4))[0]

    def _set_size(self, value):
        self.size_map.seek(0)
        self.size_map.write(struct.pack('i', value))

    def qsize(self):
        return self._get_size()

    def empty(self):
        return self.qsize() == 0

    def close(self):
        os.close(self.read_fd)
        os.close(self.write_fd)
        self.size_map.close()
        os.close(self.shm_fd)
        try:
            os.unlink('/dev/shm/queue_size')
        except:
            pass


class Empty(Exception):
    pass