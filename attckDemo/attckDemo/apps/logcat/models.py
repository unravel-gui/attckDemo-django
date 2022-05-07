# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `# 设置表名` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# 给hostip加外键
from host.models import Host


class AppcompatShims(models.Model):
    # hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    executable = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    install_time = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    sdb_id = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'appcompat_shims'


class ArpCache(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    address = models.CharField(max_length=200, blank=True, null=True)
    mac = models.CharField(max_length=200, blank=True, null=True)
    interface = models.CharField(max_length=200, blank=True, null=True)
    permanent = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'arp_cache'


class AtomPackages(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    license = models.CharField(max_length=200, blank=True, null=True)
    homepage = models.CharField(max_length=200, blank=True, null=True)
    uid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'atom_packages'


class Authenticode(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    path = models.CharField(max_length=200, blank=True, null=True)
    original_program_name = models.CharField(max_length=200, blank=True, null=True)
    serial_number = models.CharField(max_length=200, blank=True, null=True)
    issuer_name = models.CharField(max_length=200, blank=True, null=True)
    subject_name = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'authenticode'


class Autoexec(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    path = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    source = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'autoexec'


class AzureInstanceMetadata(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    location = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    offer = models.CharField(max_length=200, blank=True, null=True)
    publisher = models.CharField(max_length=200, blank=True, null=True)
    sku = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    os_type = models.CharField(max_length=200, blank=True, null=True)
    platform_update_domain = models.CharField(max_length=200, blank=True, null=True)
    platform_fault_domain = models.CharField(max_length=200, blank=True, null=True)
    vm_id = models.CharField(max_length=200, blank=True, null=True)
    vm_size = models.CharField(max_length=200, blank=True, null=True)
    subscription_id = models.CharField(max_length=200, blank=True, null=True)
    resource_group_name = models.CharField(max_length=200, blank=True, null=True)
    placement_group_id = models.CharField(max_length=200, blank=True, null=True)
    vm_scale_set_name = models.CharField(max_length=200, blank=True, null=True)
    zone = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'azure_instance_metadata'


class AzureInstanceTags(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    vm_id = models.CharField(max_length=200, blank=True, null=True)
    key = models.CharField(max_length=200, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'azure_instance_tags'


class BackgroundActivitiesModerator(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    path = models.CharField(max_length=200, blank=True, null=True)
    last_execution_time = models.BigIntegerField(blank=True, null=True)
    sid = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'background_activities_moderator'


class BitlockerInfo(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    device_id = models.CharField(max_length=200, blank=True, null=True)
    drive_letter = models.CharField(max_length=200, blank=True, null=True)
    persistent_volume_id = models.CharField(max_length=200, blank=True, null=True)
    conversion_status = models.IntegerField(blank=True, null=True)
    protection_status = models.IntegerField(blank=True, null=True)
    encryption_method = models.CharField(max_length=200, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    percentage_encrypted = models.IntegerField(blank=True, null=True)
    lock_status = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'bitlocker_info'


class CarbonBlackInfo(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    sensor_id = models.IntegerField(blank=True, null=True)
    config_name = models.CharField(max_length=200, blank=True, null=True)
    collect_store_files = models.IntegerField(blank=True, null=True)
    collect_module_loads = models.IntegerField(blank=True, null=True)
    collect_module_info = models.IntegerField(blank=True, null=True)
    collect_file_mods = models.IntegerField(blank=True, null=True)
    collect_reg_mods = models.IntegerField(blank=True, null=True)
    collect_net_conns = models.IntegerField(blank=True, null=True)
    collect_processes = models.IntegerField(blank=True, null=True)
    collect_cross_processes = models.IntegerField(blank=True, null=True)
    collect_emet_events = models.IntegerField(blank=True, null=True)
    collect_data_file_writes = models.IntegerField(blank=True, null=True)
    collect_process_user_context = models.IntegerField(blank=True, null=True)
    collect_sensor_operations = models.IntegerField(blank=True, null=True)
    log_file_disk_quota_mb = models.IntegerField(blank=True, null=True)
    log_file_disk_quota_percentage = models.IntegerField(blank=True, null=True)
    protection_disabled = models.IntegerField(blank=True, null=True)
    sensor_ip_addr = models.CharField(max_length=200, blank=True, null=True)
    sensor_backend_server = models.CharField(max_length=200, blank=True, null=True)
    event_queue = models.IntegerField(blank=True, null=True)
    binary_queue = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'carbon_black_info'


class Carves(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    time = models.BigIntegerField(blank=True, null=True)
    sha256 = models.CharField(max_length=200, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    carve_guid = models.CharField(max_length=200, blank=True, null=True)
    request_id = models.CharField(max_length=200, blank=True, null=True)
    carve = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'carves'


class Certificates(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    common_name = models.CharField(max_length=200, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    issuer = models.CharField(max_length=200, blank=True, null=True)
    ca = models.IntegerField(blank=True, null=True)
    self_signed = models.IntegerField(blank=True, null=True)
    not_valid_before = models.CharField(max_length=200, blank=True, null=True)
    not_valid_after = models.CharField(max_length=200, blank=True, null=True)
    signing_algorithm = models.CharField(max_length=200, blank=True, null=True)
    key_algorithm = models.CharField(max_length=200, blank=True, null=True)
    key_strength = models.CharField(max_length=200, blank=True, null=True)
    key_usage = models.CharField(max_length=200, blank=True, null=True)
    subject_key_id = models.CharField(max_length=200, blank=True, null=True)
    authority_key_id = models.CharField(max_length=200, blank=True, null=True)
    sha1 = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    serial = models.CharField(max_length=200, blank=True, null=True)
    sid = models.CharField(max_length=200, blank=True, null=True)
    store_location = models.CharField(max_length=200, blank=True, null=True)
    store = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    store_id = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'certificates'


class ChassisInfo(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    audible_alarm = models.CharField(max_length=200, blank=True, null=True)
    breach_description = models.CharField(max_length=200, blank=True, null=True)
    chassis_types = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    lock = models.CharField(max_length=200, blank=True, null=True)
    manufacturer = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)
    security_breach = models.CharField(max_length=200, blank=True, null=True)
    serial = models.CharField(max_length=200, blank=True, null=True)
    smbios_tag = models.CharField(max_length=200, blank=True, null=True)
    sku = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    visible_alarm = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'chassis_info'


class ChocolateyPackages(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    summary = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    license = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'chocolatey_packages'


class ChromeExtensionContentScripts(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    browser_type = models.CharField(max_length=200, blank=True, null=True)
    uid = models.BigIntegerField(blank=True, null=True)
    identifier = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    script = models.CharField(max_length=200, blank=True, null=True)
    match = models.CharField(max_length=200, blank=True, null=True)
    profile_path = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    referenced = models.BigIntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'chrome_extension_content_scripts'


class ChromeExtensions(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    browser_type = models.CharField(max_length=200, blank=True, null=True)
    uid = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    profile = models.CharField(max_length=200, blank=True, null=True)
    profile_path = models.CharField(max_length=200, blank=True, null=True)
    referenced_identifier = models.CharField(max_length=200, blank=True, null=True)
    identifier = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    default_locale = models.CharField(max_length=200, blank=True, null=True)
    current_locale = models.CharField(max_length=200, blank=True, null=True)
    update_url = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    persistent = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    permissions = models.CharField(max_length=200, blank=True, null=True)
    permissions_json = models.CharField(max_length=200, blank=True, null=True)
    optional_permissions = models.CharField(max_length=200, blank=True, null=True)
    optional_permissions_json = models.CharField(max_length=200, blank=True, null=True)
    manifest_hash = models.CharField(max_length=200, blank=True, null=True)
    referenced = models.BigIntegerField(blank=True, null=True)
    from_webstore = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    install_time = models.CharField(max_length=200, blank=True, null=True)
    install_timestamp = models.BigIntegerField(blank=True, null=True)
    manifest_json = models.CharField(max_length=200, blank=True, null=True)
    key = models.CharField(max_length=200, blank=True, null=True)
    locale = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'chrome_extensions'


class Connectivity(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    disconnected = models.IntegerField(blank=True, null=True)
    ipv4_no_traffic = models.IntegerField(blank=True, null=True)
    ipv6_no_traffic = models.IntegerField(blank=True, null=True)
    ipv4_subnet = models.IntegerField(blank=True, null=True)
    ipv4_local_network = models.IntegerField(blank=True, null=True)
    ipv4_internet = models.IntegerField(blank=True, null=True)
    ipv6_subnet = models.IntegerField(blank=True, null=True)
    ipv6_local_network = models.IntegerField(blank=True, null=True)
    ipv6_internet = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'connectivity'


class CpuInfo(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    device_id = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)
    manufacturer = models.CharField(max_length=200, blank=True, null=True)
    processor_type = models.CharField(max_length=200, blank=True, null=True)
    availability = models.CharField(max_length=200, blank=True, null=True)
    cpu_status = models.IntegerField(blank=True, null=True)
    number_of_cores = models.CharField(max_length=200, blank=True, null=True)
    logical_processors = models.IntegerField(blank=True, null=True)
    address_width = models.CharField(max_length=200, blank=True, null=True)
    current_clock_speed = models.IntegerField(blank=True, null=True)
    max_clock_speed = models.IntegerField(blank=True, null=True)
    socket_designation = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'cpu_info'


class Cpuid(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    feature = models.CharField(max_length=200, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)
    output_register = models.CharField(max_length=200, blank=True, null=True)
    output_bit = models.IntegerField(blank=True, null=True)
    input_eax = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'cpuid'


class Curl(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    url = models.CharField(max_length=200, blank=True, null=True)
    method = models.CharField(max_length=200, blank=True, null=True)
    user_agent = models.CharField(max_length=200, blank=True, null=True)
    response_code = models.IntegerField(blank=True, null=True)
    round_trip_time = models.BigIntegerField(blank=True, null=True)
    bytes = models.BigIntegerField(blank=True, null=True)
    result = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'curl'


class CurlCertificate(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    hostname = models.CharField(max_length=200, blank=True, null=True)
    common_name = models.CharField(max_length=200, blank=True, null=True)
    organization = models.CharField(max_length=200, blank=True, null=True)
    organization_unit = models.CharField(max_length=200, blank=True, null=True)
    serial_number = models.CharField(max_length=200, blank=True, null=True)
    issuer_common_name = models.CharField(max_length=200, blank=True, null=True)
    issuer_organization = models.CharField(max_length=200, blank=True, null=True)
    issuer_organization_unit = models.CharField(max_length=200, blank=True, null=True)
    valid_from = models.CharField(max_length=200, blank=True, null=True)
    valid_to = models.CharField(max_length=200, blank=True, null=True)
    sha256_fingerprint = models.CharField(max_length=200, blank=True, null=True)
    sha1_fingerprint = models.CharField(max_length=200, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    signature_algorithm = models.CharField(max_length=200, blank=True, null=True)
    signature = models.CharField(max_length=200, blank=True, null=True)
    subject_key_identifier = models.CharField(max_length=200, blank=True, null=True)
    authority_key_identifier = models.CharField(max_length=200, blank=True, null=True)
    key_usage = models.CharField(max_length=200, blank=True, null=True)
    extended_key_usage = models.CharField(max_length=200, blank=True, null=True)
    policies = models.CharField(max_length=200, blank=True, null=True)
    subject_alternative_names = models.CharField(max_length=200, blank=True, null=True)
    issuer_alternative_names = models.CharField(max_length=200, blank=True, null=True)
    info_access = models.CharField(max_length=200, blank=True, null=True)
    subject_info_access = models.CharField(max_length=200, blank=True, null=True)
    policy_mappings = models.CharField(max_length=200, blank=True, null=True)
    has_expired = models.IntegerField(blank=True, null=True)
    basic_constraint = models.CharField(max_length=200, blank=True, null=True)
    name_constraints = models.CharField(max_length=200, blank=True, null=True)
    policy_constraints = models.CharField(max_length=200, blank=True, null=True)
    dump_certificate = models.IntegerField(blank=True, null=True)
    timeout = models.IntegerField(blank=True, null=True)
    pem = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'curl_certificate'


class DefaultEnvironment(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    variable = models.CharField(max_length=200, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)
    expand = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'default_environment'


class DeviceFile(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    device = models.CharField(max_length=200, blank=True, null=True)
    partition = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    filename = models.CharField(max_length=200, blank=True, null=True)
    inode = models.BigIntegerField(blank=True, null=True)
    uid = models.BigIntegerField(blank=True, null=True)
    gid = models.BigIntegerField(blank=True, null=True)
    mode = models.CharField(max_length=200, blank=True, null=True)
    size = models.BigIntegerField(blank=True, null=True)
    block_size = models.IntegerField(blank=True, null=True)
    atime = models.BigIntegerField(blank=True, null=True)
    mtime = models.BigIntegerField(blank=True, null=True)
    ctime = models.BigIntegerField(blank=True, null=True)
    hard_links = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'device_file'


class DeviceHash(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    device = models.CharField(max_length=200, blank=True, null=True)
    partition = models.CharField(max_length=200, blank=True, null=True)
    inode = models.BigIntegerField(blank=True, null=True)
    md5 = models.CharField(max_length=200, blank=True, null=True)
    sha1 = models.CharField(max_length=200, blank=True, null=True)
    sha256 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'device_hash'


class DevicePartitions(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    device = models.CharField(max_length=200, blank=True, null=True)
    partition = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    offset = models.BigIntegerField(blank=True, null=True)
    blocks_size = models.BigIntegerField(blank=True, null=True)
    blocks = models.BigIntegerField(blank=True, null=True)
    inodes = models.BigIntegerField(blank=True, null=True)
    flags = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'device_partitions'


class DiskInfo(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    partitions = models.IntegerField(blank=True, null=True)
    disk_index = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    id = models.CharField(max_length=200, blank=True, primary_key=True)
    pnp_device_id = models.CharField(max_length=200, blank=True, null=True)
    disk_size = models.BigIntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=200, blank=True, null=True)
    hardware_model = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    serial = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'disk_info'


class DnsCache(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    flags = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'dns_cache'


class Drivers(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    device_id = models.CharField(max_length=200, blank=True, null=True)
    device_name = models.CharField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    service = models.CharField(max_length=200, blank=True, null=True)
    service_key = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    inf = models.CharField(max_length=200, blank=True, null=True)
    class_field = models.CharField(max_length=200, db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    provider = models.CharField(max_length=200, blank=True, null=True)
    manufacturer = models.CharField(max_length=200, blank=True, null=True)
    driver_key = models.CharField(max_length=200, blank=True, null=True)
    date = models.BigIntegerField(blank=True, null=True)
    signed = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'drivers'


class Ec2InstanceMetadata(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    instance_id = models.CharField(max_length=200, blank=True, null=True)
    instance_type = models.CharField(max_length=200, blank=True, null=True)
    architecture = models.CharField(max_length=200, blank=True, null=True)
    region = models.CharField(max_length=200, blank=True, null=True)
    availability_zone = models.CharField(max_length=200, blank=True, null=True)
    local_hostname = models.CharField(max_length=200, blank=True, null=True)
    local_ipv4 = models.CharField(max_length=200, blank=True, null=True)
    mac = models.CharField(max_length=200, blank=True, null=True)
    security_groups = models.CharField(max_length=200, blank=True, null=True)
    iam_arn = models.CharField(max_length=200, blank=True, null=True)
    ami_id = models.CharField(max_length=200, blank=True, null=True)
    reservation_id = models.CharField(max_length=200, blank=True, null=True)
    account_id = models.CharField(max_length=200, blank=True, null=True)
    ssh_public_key = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'ec2_instance_metadata'


class Ec2InstanceTags(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    instance_id = models.CharField(max_length=200, blank=True, null=True)
    key = models.CharField(max_length=200, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'ec2_instance_tags'


class EtcHosts(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    address = models.CharField(max_length=200, blank=True, null=True)
    hostnames = models.CharField(max_length=200, blank=True, null=True)
    pid_with_namespace = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'etc_hosts'


class EtcProtocols(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    alias = models.CharField(max_length=200, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'etc_protocols'


class EtcServices(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    protocol = models.CharField(max_length=200, blank=True, null=True)
    aliases = models.CharField(max_length=200, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'etc_services'


class File(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    path = models.CharField(max_length=200, blank=True, null=True)
    directory = models.CharField(max_length=200, blank=True, null=True)
    filename = models.CharField(max_length=200, blank=True, null=True)
    inode = models.BigIntegerField(blank=True, null=True)
    uid = models.BigIntegerField(blank=True, null=True)
    gid = models.BigIntegerField(blank=True, null=True)
    mode = models.CharField(max_length=200, blank=True, null=True)
    device = models.BigIntegerField(blank=True, null=True)
    size = models.BigIntegerField(blank=True, null=True)
    block_size = models.IntegerField(blank=True, null=True)
    atime = models.BigIntegerField(blank=True, null=True)
    mtime = models.BigIntegerField(blank=True, null=True)
    ctime = models.BigIntegerField(blank=True, null=True)
    btime = models.BigIntegerField(blank=True, null=True)
    hard_links = models.IntegerField(blank=True, null=True)
    symlink = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    attributes = models.CharField(max_length=200, blank=True, null=True)
    volume_serial = models.CharField(max_length=200, blank=True, null=True)
    file_id = models.CharField(max_length=200, blank=True, null=True)
    file_version = models.CharField(max_length=200, blank=True, null=True)
    product_version = models.CharField(max_length=200, blank=True, null=True)
    bsd_flags = models.CharField(max_length=200, blank=True, null=True)
    pid_with_namespace = models.IntegerField(blank=True, null=True)
    mount_namespace_id = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'file'


class FirefoxAddons(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    uid = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    identifier = models.CharField(max_length=200, blank=True, null=True)
    creator = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    source_url = models.CharField(max_length=200, blank=True, null=True)
    visible = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    disabled = models.IntegerField(blank=True, null=True)
    autoupdate = models.IntegerField(blank=True, null=True)
    native = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'firefox_addons'


class Groups(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    gid = models.BigIntegerField(blank=True, null=True)
    gid_signed = models.BigIntegerField(blank=True, null=True)
    groupname = models.CharField(max_length=200, blank=True, null=True)
    group_sid = models.CharField(max_length=200, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    is_field = models.IntegerField(db_column='is_', blank=True, null=True)  # Field renamed because it ended with '_'.
    pid_with_namespace = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'groups'


class Hash(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    path = models.CharField(max_length=200, blank=True, null=True)
    directory = models.CharField(max_length=200, blank=True, null=True)
    md5 = models.CharField(max_length=200, blank=True, null=True)
    sha1 = models.CharField(max_length=200, blank=True, null=True)
    sha256 = models.CharField(max_length=200, blank=True, null=True)
    ssdeep = models.CharField(max_length=200, blank=True, null=True)
    pid_with_namespace = models.IntegerField(blank=True, null=True)
    mount_namespace_id = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'hash'


class HvciStatus(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    version = models.CharField(max_length=200, blank=True, null=True)
    instance_identifier = models.CharField(max_length=200, blank=True, null=True)
    vbs_status = models.CharField(max_length=200, blank=True, null=True)
    code_integrity_policy_enforcement_status = models.CharField(max_length=200, blank=True, null=True)
    umci_policy_status = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'hvci_status'


class IeExtensions(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    registry_path = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'ie_extensions'


class IntelMeInfo(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    version = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'intel_me_info'


class InterfaceAddresses(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    interface = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    mask = models.CharField(max_length=200, blank=True, null=True)
    broadcast = models.CharField(max_length=200, blank=True, null=True)
    point_to_point = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    friendly_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'interface_addresses'


class InterfaceDetails(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    interface = models.CharField(max_length=200, blank=True, null=True)
    mac = models.CharField(max_length=200, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    mtu = models.IntegerField(blank=True, null=True)
    metric = models.IntegerField(blank=True, null=True)
    flags = models.IntegerField(blank=True, null=True)
    ipackets = models.BigIntegerField(blank=True, null=True)
    opackets = models.BigIntegerField(blank=True, null=True)
    ibytes = models.BigIntegerField(blank=True, null=True)
    obytes = models.BigIntegerField(blank=True, null=True)
    ierrors = models.BigIntegerField(blank=True, null=True)
    oerrors = models.BigIntegerField(blank=True, null=True)
    idrops = models.BigIntegerField(blank=True, null=True)
    odrops = models.BigIntegerField(blank=True, null=True)
    collisions = models.BigIntegerField(blank=True, null=True)
    last_change = models.BigIntegerField(blank=True, null=True)
    link_speed = models.BigIntegerField(blank=True, null=True)
    pci_slot = models.CharField(max_length=200, blank=True, null=True)
    friendly_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    manufacturer = models.CharField(max_length=200, blank=True, null=True)
    connection_id = models.CharField(max_length=200, blank=True, null=True)
    connection_status = models.CharField(max_length=200, blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    physical_adapter = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    service = models.CharField(max_length=200, blank=True, null=True)
    dhcp_enabled = models.IntegerField(blank=True, null=True)
    dhcp_lease_expires = models.CharField(max_length=200, blank=True, null=True)
    dhcp_lease_obtained = models.CharField(max_length=200, blank=True, null=True)
    dhcp_server = models.CharField(max_length=200, blank=True, null=True)
    dns_domain = models.CharField(max_length=200, blank=True, null=True)
    dns_domain_suffix_search_order = models.CharField(max_length=200, blank=True, null=True)
    dns_host_name = models.CharField(max_length=200, blank=True, null=True)
    dns_server_search_order = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'interface_details'


class KernelInfo(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    version = models.CharField(max_length=200, blank=True, null=True)
    arguments = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    device = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'kernel_info'


class KvaSpeculativeInfo(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    kva_shadow_enabled = models.IntegerField(blank=True, null=True)
    kva_shadow_user_global = models.IntegerField(blank=True, null=True)
    kva_shadow_pcid = models.IntegerField(blank=True, null=True)
    kva_shadow_inv_pcid = models.IntegerField(blank=True, null=True)
    bp_mitigations = models.IntegerField(blank=True, null=True)
    bp_system_pol_disabled = models.IntegerField(blank=True, null=True)
    bp_microcode_disabled = models.IntegerField(blank=True, null=True)
    cpu_spec_ctrl_supported = models.IntegerField(blank=True, null=True)
    ibrs_support_enabled = models.IntegerField(blank=True, null=True)
    stibp_support_enabled = models.IntegerField(blank=True, null=True)
    cpu_pred_cmd_supported = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'kva_speculative_info'


class ListeningPorts(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    pid = models.IntegerField(blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    protocol = models.IntegerField(blank=True, null=True)
    family = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    fd = models.BigIntegerField(blank=True, null=True)
    socket = models.BigIntegerField(blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    net_namespace = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'listening_ports'


class LoggedInUsers(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    type = models.CharField(max_length=200, blank=True, null=True)
    user = models.CharField(max_length=200, blank=True, null=True)
    tty = models.CharField(max_length=200, blank=True, null=True)
    host = models.CharField(max_length=200, blank=True, null=True)
    time = models.BigIntegerField(blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    sid = models.CharField(max_length=200, blank=True, null=True)
    registry_hive = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'logged_in_users'


class LogicalDrives(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    device_id = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    free_space = models.BigIntegerField(blank=True, null=True)
    size = models.BigIntegerField(blank=True, null=True)
    file_system = models.CharField(max_length=200, blank=True, null=True)
    boot_partition = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'logical_drives'


class LogonSessions(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    logon_id = models.IntegerField(blank=True, null=True)
    user = models.CharField(max_length=200, blank=True, null=True)
    logon_domain = models.CharField(max_length=200, blank=True, null=True)
    authentication_package = models.CharField(max_length=200, blank=True, null=True)
    logon_type = models.CharField(max_length=200, blank=True, null=True)
    session_id = models.IntegerField(blank=True, null=True)
    logon_sid = models.CharField(max_length=200, blank=True, null=True)
    logon_time = models.BigIntegerField(blank=True, null=True)
    logon_server = models.CharField(max_length=200, blank=True, null=True)
    dns_domain_name = models.CharField(max_length=200, blank=True, null=True)
    upn = models.CharField(max_length=200, blank=True, null=True)
    logon_script = models.CharField(max_length=200, blank=True, null=True)
    profile_path = models.CharField(max_length=200, blank=True, null=True)
    home_directory = models.CharField(max_length=200, blank=True, null=True)
    home_directory_drive = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'logon_sessions'


class Ntdomains(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    client_site_name = models.CharField(max_length=200, blank=True, null=True)
    dc_site_name = models.CharField(max_length=200, blank=True, null=True)
    dns_forest_name = models.CharField(max_length=200, blank=True, null=True)
    domain_controller_address = models.CharField(max_length=200, blank=True, null=True)
    domain_controller_name = models.CharField(max_length=200, blank=True, null=True)
    domain_name = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'ntdomains'


class NtfsAclPermissions(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    path = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    principal = models.CharField(max_length=200, blank=True, null=True)
    access = models.CharField(max_length=200, blank=True, null=True)
    inherited_from = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'ntfs_acl_permissions'


class NtfsJournalEvents(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    action = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    old_path = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    record_timestamp = models.CharField(max_length=200, blank=True, null=True)
    record_usn = models.CharField(max_length=200, blank=True, null=True)
    node_ref_number = models.CharField(max_length=200, blank=True, null=True)
    parent_ref_number = models.CharField(max_length=200, blank=True, null=True)
    drive_letter = models.CharField(max_length=200, blank=True, null=True)
    file_attributes = models.CharField(max_length=200, blank=True, null=True)
    partial = models.BigIntegerField(blank=True, null=True)
    time = models.BigIntegerField(blank=True, null=True)
    eid = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'ntfs_journal_events'


class OfficeMru(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    application = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    last_opened_time = models.BigIntegerField(blank=True, null=True)
    sid = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'office_mru'


class OsVersion(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    minor = models.IntegerField(blank=True, null=True)
    patch = models.IntegerField(blank=True, null=True)
    build = models.CharField(max_length=200, blank=True, null=True)
    platform = models.CharField(max_length=200, blank=True, null=True)
    platform_like = models.CharField(max_length=200, blank=True, null=True)
    codename = models.CharField(max_length=200, blank=True, null=True)
    arch = models.CharField(max_length=200, blank=True, null=True)
    install_date = models.BigIntegerField(blank=True, null=True)
    pid_with_namespace = models.IntegerField(blank=True, null=True)
    mount_namespace_id = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'os_version'


class OsqueryEvents(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    publisher = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    subscriptions = models.IntegerField(blank=True, null=True)
    events = models.IntegerField(blank=True, null=True)
    refreshes = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'osquery_events'


class OsqueryExtensions(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    uuid = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    sdk_version = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'osquery_extensions'


class OsqueryFlags(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    default_value = models.CharField(max_length=200, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)
    shell_only = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'osquery_flags'


class OsqueryInfo(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    pid = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=200, blank=True, null=True)
    instance_id = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    config_hash = models.CharField(max_length=200, blank=True, null=True)
    config_valid = models.IntegerField(blank=True, null=True)
    extensions = models.CharField(max_length=200, blank=True, null=True)
    build_platform = models.CharField(max_length=200, blank=True, null=True)
    build_distro = models.CharField(max_length=200, blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    watcher = models.IntegerField(blank=True, null=True)
    platform_mask = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'osquery_info'


class OsqueryPacks(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    platform = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    shard = models.IntegerField(blank=True, null=True)
    discovery_cache_hits = models.IntegerField(blank=True, null=True)
    discovery_executions = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'osquery_packs'


class OsqueryRegistry(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    registry = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    owner_uuid = models.IntegerField(blank=True, null=True)
    internal = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'osquery_registry'


class OsquerySchedule(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    query = models.CharField(max_length=200, blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)
    executions = models.BigIntegerField(blank=True, null=True)
    last_executed = models.BigIntegerField(blank=True, null=True)
    denylisted = models.IntegerField(blank=True, null=True)
    output_size = models.BigIntegerField(blank=True, null=True)
    wall_time = models.BigIntegerField(blank=True, null=True)
    user_time = models.BigIntegerField(blank=True, null=True)
    system_time = models.BigIntegerField(blank=True, null=True)
    average_memory = models.BigIntegerField(blank=True, null=True)
    blacklisted = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'osquery_schedule'


class Patches(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    csname = models.CharField(max_length=200, blank=True, null=True)
    hotfix_id = models.CharField(max_length=200, blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    fix_comments = models.CharField(max_length=200, blank=True, null=True)
    installed_by = models.CharField(max_length=200, blank=True, null=True)
    install_date = models.CharField(max_length=200, blank=True, null=True)
    installed_on = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'patches'


class PhysicalDiskPerformance(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    avg_disk_bytes_per_read = models.BigIntegerField(blank=True, null=True)
    avg_disk_bytes_per_write = models.BigIntegerField(blank=True, null=True)
    avg_disk_read_queue_length = models.BigIntegerField(blank=True, null=True)
    avg_disk_write_queue_length = models.BigIntegerField(blank=True, null=True)
    avg_disk_sec_per_read = models.IntegerField(blank=True, null=True)
    avg_disk_sec_per_write = models.IntegerField(blank=True, null=True)
    current_disk_queue_length = models.IntegerField(blank=True, null=True)
    percent_disk_read_time = models.BigIntegerField(blank=True, null=True)
    percent_disk_write_time = models.BigIntegerField(blank=True, null=True)
    percent_disk_time = models.BigIntegerField(blank=True, null=True)
    percent_idle_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'physical_disk_performance'


class Pipes(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    pid = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    instances = models.IntegerField(blank=True, null=True)
    max_instances = models.IntegerField(blank=True, null=True)
    flags = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'pipes'


class PlatformInfo(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    vendor = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    date = models.CharField(max_length=200, blank=True, null=True)
    revision = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    size = models.CharField(max_length=200, blank=True, null=True)
    volume_size = models.IntegerField(blank=True, null=True)
    extra = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'platform_info'


class PowershellEvents(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    time = models.BigIntegerField(blank=True, null=True)
    datetime = models.CharField(max_length=200, blank=True, null=True)
    script_block_id = models.CharField(max_length=200, blank=True, null=True)
    script_block_count = models.IntegerField(blank=True, null=True)
    script_text = models.CharField(max_length=200, blank=True, null=True)
    script_name = models.CharField(max_length=200, blank=True, null=True)
    script_path = models.CharField(max_length=200, blank=True, null=True)
    cosine_similarity = models.FloatField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'powershell_events'


class Prefetch(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    path = models.CharField(max_length=200, blank=True, null=True)
    filename = models.CharField(max_length=200, blank=True, null=True)
    hash = models.CharField(max_length=200, blank=True, null=True)
    last_run_time = models.IntegerField(blank=True, null=True)
    other_run_times = models.CharField(max_length=200, blank=True, null=True)
    run_count = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    volume_serial = models.CharField(max_length=200, blank=True, null=True)
    volume_creation = models.CharField(max_length=200, blank=True, null=True)
    accessed_files_count = models.IntegerField(blank=True, null=True)
    accessed_directories_count = models.IntegerField(blank=True, null=True)
    accessed_files = models.CharField(max_length=200, blank=True, null=True)
    accessed_directories = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'prefetch'


class ProcessMemoryMap(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    pid = models.IntegerField(blank=True, null=True)
    start = models.CharField(max_length=200, blank=True, null=True)
    end = models.CharField(max_length=200, blank=True, null=True)
    permissions = models.CharField(max_length=200, blank=True, null=True)
    offset = models.BigIntegerField(blank=True, null=True)
    device = models.CharField(max_length=200, blank=True, null=True)
    inode = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    pseudo = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'process_memory_map'


class ProcessOpenSockets(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    pid = models.IntegerField(blank=True, null=True)
    fd = models.BigIntegerField(blank=True, null=True)
    socket = models.BigIntegerField(blank=True, null=True)
    family = models.IntegerField(blank=True, null=True)
    protocol = models.IntegerField(blank=True, null=True)
    local_address = models.CharField(max_length=200, blank=True, null=True)
    remote_address = models.CharField(max_length=200, blank=True, null=True)
    local_port = models.IntegerField(blank=True, null=True)
    remote_port = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    net_namespace = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'process_open_sockets'


class Processes(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    pid = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    cmdline = models.TextField(max_length=8000)
    state = models.CharField(max_length=200, blank=True, null=True)
    cwd = models.CharField(max_length=200, blank=True, null=True)
    root = models.CharField(max_length=200, blank=True, null=True)
    uid = models.BigIntegerField(blank=True, null=True)
    gid = models.BigIntegerField(blank=True, null=True)
    euid = models.BigIntegerField(blank=True, null=True)
    egid = models.BigIntegerField(blank=True, null=True)
    suid = models.BigIntegerField(blank=True, null=True)
    sgid = models.BigIntegerField(blank=True, null=True)
    on_disk = models.IntegerField(blank=True, null=True)
    wired_size = models.BigIntegerField(blank=True, null=True)
    resident_size = models.BigIntegerField(blank=True, null=True)
    total_size = models.BigIntegerField(blank=True, null=True)
    user_time = models.BigIntegerField(blank=True, null=True)
    system_time = models.BigIntegerField(blank=True, null=True)
    disk_bytes_read = models.BigIntegerField(blank=True, null=True)
    disk_bytes_written = models.BigIntegerField(blank=True, null=True)
    start_time = models.BigIntegerField(blank=True, null=True)
    parent = models.BigIntegerField(blank=True, null=True)
    pgroup = models.BigIntegerField(blank=True, null=True)
    threads = models.IntegerField(blank=True, null=True)
    nice = models.IntegerField(blank=True, null=True)
    elevated_token = models.IntegerField(blank=True, null=True)
    secure_process = models.IntegerField(blank=True, null=True)
    protection_type = models.CharField(max_length=200, blank=True, null=True)
    virtual_process = models.IntegerField(blank=True, null=True)
    elapsed_time = models.BigIntegerField(blank=True, null=True)
    handle_count = models.BigIntegerField(blank=True, null=True)
    percent_processor_time = models.BigIntegerField(blank=True, null=True)
    upid = models.BigIntegerField(blank=True, null=True)
    uppid = models.BigIntegerField(blank=True, null=True)
    cpu_type = models.IntegerField(blank=True, null=True)
    cpu_subtype = models.IntegerField(blank=True, null=True)
    phys_footprint = models.BigIntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'processes'


class Programs(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    install_location = models.CharField(max_length=200, blank=True, null=True)
    install_source = models.CharField(max_length=200, blank=True, null=True)
    language = models.CharField(max_length=200, blank=True, null=True)
    publisher = models.CharField(max_length=200, blank=True, null=True)
    uninstall_string = models.CharField(max_length=200, blank=True, null=True)
    install_date = models.CharField(max_length=200, blank=True, null=True)
    identifying_number = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'programs'


class PythonPackages(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    summary = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    license = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    directory = models.CharField(max_length=200, blank=True, null=True)
    pid_with_namespace = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'python_packages'


class Registry(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    key = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    data = models.CharField(max_length=200, blank=True, null=True)
    mtime = models.BigIntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'registry'


class Routes(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    destination = models.CharField(max_length=200, blank=True, null=True)
    netmask = models.IntegerField(blank=True, null=True)
    gateway = models.CharField(max_length=200, blank=True, null=True)
    source = models.CharField(max_length=200, blank=True, null=True)
    flags = models.IntegerField(blank=True, null=True)
    interface = models.CharField(max_length=200, blank=True, null=True)
    mtu = models.IntegerField(blank=True, null=True)
    metric = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    hopcount = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'routes'


class ScheduledTasks(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    action = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    hidden = models.IntegerField(blank=True, null=True)
    last_run_time = models.BigIntegerField(blank=True, null=True)
    next_run_time = models.BigIntegerField(blank=True, null=True)
    last_run_message = models.CharField(max_length=200, blank=True, null=True)
    last_run_code = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'scheduled_tasks'


class Secureboot(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    secure_boot = models.IntegerField(blank=True, null=True)
    setup_mode = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'secureboot'


class Services(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    service_type = models.CharField(max_length=200, blank=True, null=True)
    display_name = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    start_type = models.CharField(max_length=200, blank=True, null=True)
    win32_exit_code = models.IntegerField(blank=True, null=True)
    service_exit_code = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    module_path = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    user_account = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'services'


class SharedResources(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    description = models.CharField(max_length=200, blank=True, null=True)
    install_date = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    allow_maximum = models.IntegerField(blank=True, null=True)
    maximum_allowed = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'shared_resources'


class Shellbags(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    sid = models.CharField(max_length=200, blank=True, null=True)
    source = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    modified_time = models.BigIntegerField(blank=True, null=True)
    created_time = models.BigIntegerField(blank=True, null=True)
    accessed_time = models.BigIntegerField(blank=True, null=True)
    mft_entry = models.BigIntegerField(blank=True, null=True)
    mft_sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'shellbags'


class Shimcache(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    entry = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    modified_time = models.IntegerField(blank=True, null=True)
    execution_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'shimcache'


class ShortcutFiles(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    path = models.CharField(max_length=200, blank=True, null=True)
    target_path = models.CharField(max_length=200, blank=True, null=True)
    target_modified = models.IntegerField(blank=True, null=True)
    target_created = models.IntegerField(blank=True, null=True)
    target_accessed = models.IntegerField(blank=True, null=True)
    target_size = models.BigIntegerField(blank=True, null=True)
    relative_path = models.CharField(max_length=200, blank=True, null=True)
    local_path = models.CharField(max_length=200, blank=True, null=True)
    working_path = models.CharField(max_length=200, blank=True, null=True)
    icon_path = models.CharField(max_length=200, blank=True, null=True)
    common_path = models.CharField(max_length=200, blank=True, null=True)
    command_args = models.CharField(max_length=200, blank=True, null=True)
    hostname = models.CharField(max_length=200, blank=True, null=True)
    share_name = models.CharField(max_length=200, blank=True, null=True)
    device_type = models.CharField(max_length=200, blank=True, null=True)
    volume_serial = models.CharField(max_length=200, blank=True, null=True)
    mft_entry = models.BigIntegerField(blank=True, null=True)
    mft_sequence = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'shortcut_files'


class SshConfigs(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    uid = models.BigIntegerField(blank=True, null=True)
    block = models.CharField(max_length=200, blank=True, null=True)
    option = models.CharField(max_length=200, blank=True, null=True)
    ssh_config_file = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'ssh_configs'


class StartupItems(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    args = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    source = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'startup_items'


class SystemInfo(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    hostname = models.CharField(max_length=200, blank=True, null=True)
    uuid = models.CharField(max_length=200, blank=True, null=True)
    cpu_type = models.CharField(max_length=200, blank=True, null=True)
    cpu_subtype = models.CharField(max_length=200, blank=True, null=True)
    cpu_brand = models.CharField(max_length=200, blank=True, null=True)
    cpu_physical_cores = models.IntegerField(blank=True, null=True)
    cpu_logical_cores = models.IntegerField(blank=True, null=True)
    cpu_microcode = models.CharField(max_length=200, blank=True, null=True)
    physical_memory = models.BigIntegerField(blank=True, null=True)
    hardware_vendor = models.CharField(max_length=200, blank=True, null=True)
    hardware_model = models.CharField(max_length=200, blank=True, null=True)
    hardware_version = models.CharField(max_length=200, blank=True, null=True)
    hardware_serial = models.CharField(max_length=200, blank=True, null=True)
    board_vendor = models.CharField(max_length=200, blank=True, null=True)
    board_model = models.CharField(max_length=200, blank=True, null=True)
    board_version = models.CharField(max_length=200, blank=True, null=True)
    board_serial = models.CharField(max_length=200, blank=True, null=True)
    computer_name = models.CharField(max_length=200, blank=True, null=True)
    local_hostname = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'system_info'


class Time(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    weekday = models.CharField(max_length=200, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    seconds = models.IntegerField(blank=True, null=True)
    timezone = models.CharField(max_length=200, blank=True, null=True)
    local_timezone = models.CharField(max_length=200, blank=True, null=True)
    unix_time = models.IntegerField(blank=True, null=True)
    timestamp = models.CharField(max_length=200, blank=True, null=True)
    datetime = models.CharField(max_length=200, blank=True, null=True)
    iso_8601 = models.CharField(max_length=200, blank=True, null=True)
    win_timestamp = models.BigIntegerField(blank=True, null=True)
    date_time = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'time'


class TpmInfo(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    activated = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    owned = models.IntegerField(blank=True, null=True)
    manufacturer_version = models.CharField(max_length=200, blank=True, null=True)
    manufacturer_id = models.IntegerField(blank=True, null=True)
    manufacturer_name = models.CharField(max_length=200, blank=True, null=True)
    product_name = models.CharField(max_length=200, blank=True, null=True)
    physical_presence_version = models.CharField(max_length=200, blank=True, null=True)
    spec_version = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'tpm_info'


class Uptime(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    days = models.IntegerField(blank=True, null=True)
    hours = models.IntegerField(blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    seconds = models.IntegerField(blank=True, null=True)
    total_seconds = models.BigIntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'uptime'


class UserGroups(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    uid = models.BigIntegerField(blank=True, null=True)
    gid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'user_groups'


class UserSshKeys(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    uid = models.BigIntegerField(blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    encrypted = models.IntegerField(blank=True, null=True)
    key_type = models.CharField(max_length=200, blank=True, null=True)
    pid_with_namespace = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'user_ssh_keys'


class Userassist(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    path = models.CharField(max_length=200, blank=True, null=True)
    last_execution_time = models.BigIntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    sid = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'userassist'


class Users(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    uid = models.BigIntegerField(blank=True, null=True)
    gid = models.BigIntegerField(blank=True, null=True)
    uid_signed = models.BigIntegerField(blank=True, null=True)
    gid_signed = models.BigIntegerField(blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    directory = models.CharField(max_length=200, blank=True, null=True)
    shell = models.CharField(max_length=200, blank=True, null=True)
    uuid = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    is_field = models.IntegerField(db_column='is_', blank=True, null=True)  # Field renamed because it ended with '_'.
    pid_with_namespace = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'users'


class VideoInfo(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    color_depth = models.IntegerField(blank=True, null=True)
    driver = models.CharField(max_length=200, blank=True, null=True)
    driver_date = models.BigIntegerField(blank=True, null=True)
    driver_version = models.CharField(max_length=200, blank=True, null=True)
    manufacturer = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)
    series = models.CharField(max_length=200, blank=True, null=True)
    video_mode = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'video_info'


class Winbaseobj(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    session_id = models.IntegerField(blank=True, null=True)
    object_name = models.CharField(max_length=200, blank=True, null=True)
    object_type = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'winbaseobj'


class WindowsCrashes(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    datetime = models.CharField(max_length=200, blank=True, null=True)
    module = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    tid = models.BigIntegerField(blank=True, null=True)
    version = models.CharField(max_length=200, blank=True, null=True)
    process_uptime = models.BigIntegerField(blank=True, null=True)
    stack_trace = models.CharField(max_length=200, blank=True, null=True)
    exception_code = models.CharField(max_length=200, blank=True, null=True)
    exception_message = models.CharField(max_length=200, blank=True, null=True)
    exception_address = models.CharField(max_length=200, blank=True, null=True)
    registers = models.CharField(max_length=200, blank=True, null=True)
    command_line = models.CharField(max_length=200, blank=True, null=True)
    current_directory = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    machine_name = models.CharField(max_length=200, blank=True, null=True)
    major_version = models.IntegerField(blank=True, null=True)
    minor_version = models.IntegerField(blank=True, null=True)
    build_number = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    crash_path = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'windows_crashes'


class WindowsEventlog(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    channel = models.CharField(max_length=200, blank=True, null=True)
    datetime = models.CharField(max_length=200, blank=True, null=True)
    task = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    provider_name = models.CharField(max_length=200, blank=True, null=True)
    provider_guid = models.CharField(max_length=200, blank=True, null=True)
    computer_name = models.CharField(max_length=200, blank=True, null=True)
    eventid = models.IntegerField(blank=True, null=True)
    keywords = models.CharField(max_length=200, blank=True, null=True)
    data = models.CharField(max_length=200, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    tid = models.IntegerField(blank=True, null=True)
    time_range = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.CharField(max_length=200, blank=True, null=True)
    xpath = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'windows_eventlog'


class WindowsEvents(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    time = models.BigIntegerField(blank=True, null=True)
    datetime = models.CharField(max_length=200, blank=True, null=True)
    source = models.CharField(max_length=200, blank=True, null=True)
    provider_name = models.CharField(max_length=200, blank=True, null=True)
    provider_guid = models.CharField(max_length=200, blank=True, null=True)
    computer_name = models.CharField(max_length=200, blank=True, null=True)
    eventid = models.IntegerField(blank=True, null=True)
    task = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    keywords = models.CharField(max_length=200, blank=True, null=True)
    data = models.CharField(max_length=200, blank=True, null=True)
    eid = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'windows_events'


class WindowsFirewallRules(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    app_name = models.CharField(max_length=200, blank=True, null=True)
    action = models.CharField(max_length=200, blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    grouping = models.CharField(max_length=200, blank=True, null=True)
    direction = models.CharField(max_length=200, blank=True, null=True)
    protocol = models.CharField(max_length=200, blank=True, null=True)
    local_addresses = models.CharField(max_length=200, blank=True, null=True)
    remote_addresses = models.CharField(max_length=200, blank=True, null=True)
    local_ports = models.CharField(max_length=200, blank=True, null=True)
    remote_ports = models.CharField(max_length=200, blank=True, null=True)
    icmp_types_codes = models.CharField(max_length=200, blank=True, null=True)
    profile_domain = models.IntegerField(blank=True, null=True)
    profile_private = models.IntegerField(blank=True, null=True)
    profile_public = models.IntegerField(blank=True, null=True)
    service_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'windows_firewall_rules'


class WindowsOptionalFeatures(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    statename = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'windows_optional_features'


class WindowsSecurityCenter(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    firewall = models.CharField(max_length=200, blank=True, null=True)
    autoupdate = models.CharField(max_length=200, blank=True, null=True)
    antivirus = models.CharField(max_length=200, blank=True, null=True)
    antispyware = models.CharField(max_length=200, blank=True, null=True)
    internet_settings = models.CharField(max_length=200, blank=True, null=True)
    windows_security_center_service = models.CharField(max_length=200, blank=True, null=True)
    user_account_control = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'windows_security_center'


class WindowsSecurityProducts(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    type = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    state_timestamp = models.CharField(max_length=200, blank=True, null=True)
    remediation_path = models.CharField(max_length=200, blank=True, null=True)
    signatures_up_to_date = models.IntegerField(blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'windows_security_products'


class WmiBiosInfo(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'wmi_bios_info'


class WmiCliEventConsumers(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    command_line_template = models.CharField(max_length=200, blank=True, null=True)
    executable_path = models.CharField(max_length=200, blank=True, null=True)
    class_field = models.CharField(max_length=200, db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    relative_path = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'wmi_cli_event_consumers'


class WmiEventFilters(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    query = models.CharField(max_length=200, blank=True, null=True)
    query_language = models.CharField(max_length=200, blank=True, null=True)
    class_field = models.CharField(max_length=200, db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    relative_path = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'wmi_event_filters'


class WmiFilterConsumerBinding(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    consumer = models.CharField(max_length=200, blank=True, null=True)
    filter = models.CharField(max_length=200, blank=True, null=True)
    class_field = models.CharField(max_length=200, db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    relative_path = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'wmi_filter_consumer_binding'


class WmiScriptEventConsumers(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    name = models.CharField(max_length=200, blank=True, null=True)
    scripting_engine = models.CharField(max_length=200, blank=True, null=True)
    script_file_name = models.CharField(max_length=200, blank=True, null=True)
    script_text = models.CharField(max_length=200, blank=True, null=True)
    class_field = models.CharField(max_length=200, db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    relative_path = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'wmi_script_event_consumers'


class Yara(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    path = models.CharField(max_length=200, blank=True, null=True)
    matches = models.CharField(max_length=200, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    sig_group = models.CharField(max_length=200, blank=True, null=True)
    sigfile = models.CharField(max_length=200, blank=True, null=True)
    sigrule = models.CharField(max_length=200, blank=True, null=True)
    strings = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)
    sigurl = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'yara'


class YcloudInstanceMetadata(models.Model):
    hostip = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机地址')
    record_time = models.CharField(max_length=200, )
    instance_id = models.CharField(max_length=200, blank=True, null=True)
    folder_id = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    hostname = models.CharField(max_length=200, blank=True, null=True)
    zone = models.CharField(max_length=200, blank=True, null=True)
    ssh_public_key = models.CharField(max_length=200, blank=True, null=True)
    serial_port_enabled = models.CharField(max_length=200, blank=True, null=True)
    metadata_endpoint = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 'ycloud_instance_metadata'
